---
title: "Detect changes in Security posture - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes"
category: "04-API-Reference/Other"
fetched_at: "2026-11-11T06:25:23Z"
tags: ["api", "security"]
---

# Detect changes in Security posture

Copy page



Start from sample detection rules for Security posture activities in your SIEM: accepted risks, controls attested as Failed, unexpected editors, bursts of changes, and attestations that end automatically.

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude-compliance-api-access.md).

These sample rules alert on changes in your organization’s [Security posture](manage-claude-compliance-security-posture-overview.md), using the activities that the Compliance API Activity Feed records. They assume that your security information and event management (SIEM) system stores these activities, as [Send events to your SIEM](manage-claude-compliance-security-posture-send-events.md) describes.

## Before you write a rule

Each rule is a plain description and a query in no particular query language.

- Queries use the Activity Feed’s field names, plus `stored_at`, this page’s name for when you stored an activity. Any other name is your own list or alias.
- Before a rule counts activities, deduplicate them by `id`.
- Unless a rule says otherwise, run it over the time since its last completed run, by `stored_at`, not `created_at`, because an activity can arrive late; queries leave that range out.
- Write rules that fire on an activity you stored, never on one you have not: it may be late or a change [the feed does not record](manage-claude-compliance-security-posture-events-reference.md#what-the-feed-does-not-record). To compare stored activities with current results, see [Check events against results](manage-claude-compliance-security-posture-check-events-against-results.md).

## Attestation rules

These five rules read [`org_security_control_attestation_updated`](manage-claude-compliance-security-posture-events-reference.md#attestation-activity) activities.

### A risk was accepted

Alert when someone accepts the risk (`accepted_risk`) of not meeting a security control, so that a second person can review the decision.

```python
type == "org_security_control_attestation_updated"
AND status == "accepted_risk"
AND actor.type != "system_actor"
```



The rule leaves out a `system_actor`, because an automatic change, such as an attestation that ended (`lapsed`), keeps the `status` but is not an acceptance.

### A control was attested as Failed

Alert when someone attests to a control as Failed (`control_failed`), so that someone follows up on the control.

```python
type == "org_security_control_attestation_updated"
AND status == "control_failed"
AND actor.type != "system_actor"
```



The rule leaves out a `system_actor` for the same reason as [A risk was accepted](#a-risk-was-accepted).

### Someone outside an allowlist changed an attestation

Alert when an attestation is recorded, changed, saved again, or cleared by someone not on your list of people who manage attestations. Keep their `user_id` values (`allowed_user_ids`) in your SIEM.

```python
type == "org_security_control_attestation_updated"
AND actor.type != "system_actor"
AND NOT (actor.type == "user_actor" AND actor.user_id IN allowed_user_ids)
```



- Any actor other than a listed `user_actor` or a `system_actor` fires the rule.
- Key the list on `actor.user_id`: `actor.email_address` is the address the person had when the activity was recorded ([Correlate with your SIEM](manage-claude-compliance-integration-patterns.md#correlate-with-your-siem)).

### One person made many attestation changes

Alert when one person makes more attestation changes in a short time than is usual for your organization. The threshold of 10 and the 1-hour window are examples; choose both from your own activity.

```python
type == "org_security_control_attestation_updated"
AND actor.type == "user_actor"
| group by organization_uuid, actor.user_id over a sliding 1 hour of created_at
| where count(distinct id) >= 10
```



- Alert only for a group that holds an activity stored since the rule’s last run, and count over every activity that you stored, so that a late activity joins a burst whose other activities you stored earlier.
- Counting by `created_at` measures the person’s pace, not your ingestion’s.

### An attestation ended automatically

Treat a `lapsed` activity as a prompt to review the control that it names.

```python
type == "org_security_control_attestation_updated"
AND action == "lapsed"
```



A [`lapsed` activity](manage-claude-compliance-security-posture-events-reference.md#what-a-lapsed-activity-means) means that the control’s check result or its current value differs from the one the attestation was saved on, not that an end date (`review_date`) passed. It can come late.

## Keep rules working as values change

New values can appear in any of these fields.

- Identify automatic changes by `actor.type`, not by the value of `actor.service`.
- Do not drop activities whose `control`, `action`, or `status` value a rule does not list; a new `action` value can record an acceptance. See the [events reference](manage-claude-compliance-security-posture-events-reference.md).

## Test a rule

To see [the allowlist rule](#someone-outside-an-allowlist-changed-an-attestation) fire, choose someone who can attest and who is not on your list. Have that person attest to a control that has no attestation and whose result no one relies on, then clear it. Until it is cleared, the attestation can change that control’s result. Both activities can take a while to reach the Activity Feed.

If you store these activities as Open Cybersecurity Schema Framework (OCSF) events, [Map Security posture events to OCSF](manage-claude-compliance-security-posture-ocsf-mapping.md) maps their fields.
