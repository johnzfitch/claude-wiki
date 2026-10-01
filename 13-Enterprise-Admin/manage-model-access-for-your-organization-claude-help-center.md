---
title: "Manage model access for your organization | Claude Help Center"
source_url: "https://support.claude.com/en/articles/15694740"
category: "13-Enterprise-Admin"
fetched_at: "2026-09-30T06:32:09Z"
tags: ["claude-code", "enterprise"]
---

# Manage model access for your organization


This guide explains how to control which Claude models members of your organization can use, and how to cap the effort level members can select on each model. Model access and effort limits can be set for your whole organization or for specific custom roles.

Model access settings are available for Enterprise plan organizations. Primary Owners, Owners, and members whose custom role grants the Identity & Access permission can manage them in **[Organization settings \> Models](https://claude.ai/admin-settings/models)**.

To set the model new conversations start on, see **[Set a default model for your organization](set-a-default-model-for-your-organization-claude-help-center.md)**.

------------------------------------------------------------------------

## How model access works

Model access and effort limits are determined at two levels:

- **Organization level:** each model is enabled or disabled for everyone in your organization. Disabling a model here removes it for every member, including Owners and Admins. You can also set a maximum effort level for each enabled model, which applies to every member.

- **Custom role level:** for members on custom roles, each role grants access to a subset of the models enabled at the organization level. A role can also cap the maximum effort level members can select on each model, at or below the organization's cap for that model.

The organization setting is the ceiling. A role can't grant access to a model that's disabled for the organization, and a role can't allow an effort level higher than the organization's cap. When the feature first becomes available, every model is enabled and set to its highest effort level at both levels, so nothing changes for your members until you adjust these settings.

**Note:** Haiku models are always available to every member and can’t be disabled. This guarantees members always have at least one model to fall back to.

## Who each level affects

- Disabling a model or capping its effort level at the organization level affects every member, including Primary Owners, Owners, Admins, and Users.

- Role-level model access and effort limits affect only members whose role is set to "Custom." Members with the User, Admin, or Owner roles can use every model enabled at the organization level, up to the organization's effort cap for that model.

------------------------------------------------------------------------

## Enable or disable a model for your organization

1.  Navigate to **[Organization settings \> Models](https://claude.ai/admin-settings/models)**.

2.  Under **Model access**, find the model you want to change.

3.  To enable a model, switch the toggle next to it on, then click the role dropdown to select the roles that can access it.

4.  To disable a model, click the role dropdown and deselect the roles before switching the toggle off.

5.  Click "Save."

If any custom role uses the model you’re disabling as its default, you’ll be prompted to change that role’s default before the change can be saved.


------------------------------------------------------------------------

## Limit the maximum effort level for your organization

Effort limits determine how much computation members can apply per response on each model. Higher effort levels produce more thorough responses but consume more usage. An organization-level effort cap applies to every member and is the highest level any custom role can allow.

1.  Navigate to **[Organization settings \> Model](https://claude.ai/admin-settings/models)**[s](https://claude.ai/admin-settings/models).

2.  Under **Model access**, find the model you want to change.

3.  Click the effort level dropdown to select the maximum level.

4.  Click "Save."

If any custom role has an effort cap higher than the new organization cap for that model, the role's cap is lowered to match. Members see only effort levels at or below the organization cap in their model menu. Available effort levels differ depending on the model, and some models don't support effort level settings at all. For an explanation of each level, see **[Change the model, effort, and thinking settings](../15-Claude-AI-Features/how-can-i-change-the-model-version-that-i-m-chatting-with.md)**.

------------------------------------------------------------------------

## Set model access for a custom role

1.  Navigate to **[Organization settings \> Roles](https://claude.ai/admin-settings/roles)**.

2.  Click the role you want to edit, or click “Add role” to create one.

3.  Select the "Models" tab.

4.  Under **Model access**, switch each model on or off. Models disabled at the organization level appear but can’t be enabled until you turn them on for the organization.

5.  Click “Save.”

Only models the role grants access to can be selected as that role’s default model.


------------------------------------------------------------------------

## Limit the maximum effort level for a custom role

Effort limits determine how much computation members on a role can apply per response on each model. Higher effort levels produce more thorough responses but consume more usage. A role's effort cap can't be higher than the organization's cap for that model.

1.  Navigate to **[Organization settings \> Roles](https://claude.ai/admin-settings/roles)**.

2.  Click the role you want to edit.

3.  Select the "Models" tab.

4.  Next to a model, click the gear icon and choose a level.

5.  Click "Save" to save your changes.


Members on the role see only effort levels at or below the cap in their model menu. Note that available effort levels differ depending on the model, and some models don’t support effort level settings at all. For an explanation of each level, see **[Change the model, effort, and thinking settings](../15-Claude-AI-Features/how-can-i-change-the-model-version-that-i-m-chatting-with.md)**.

------------------------------------------------------------------------

## How access combines across multiple roles

If a member belongs to multiple groups with different custom roles, model settings combine like other role permissions:

- **Model access is additive.** The member can use every model granted by any of their roles, as long as it’s enabled at the organization level.

- **Effort limits take the highest cap.** For each model, the member gets the highest maximum effort level any of their roles allows, never exceeding the organization's cap for that model.

For how default models are chosen across multiple roles, see **[Set a default model for your organization](set-a-default-model-for-your-organization-claude-help-center.md)**.

For details on creating roles and assigning them to groups, see **[Manage custom roles on Enterprise plans](../17-Billing-Plans/manage-custom-roles-on-enterprise-plans.md)**.

------------------------------------------------------------------------

## What users see

In every covered product, the model picker shows only the models the member has access to. Effort levels above the organization's cap, or above a role's cap, don't appear in the effort menu.

Model availability also depends on the product. Each product supports a different set of models, so an enabled model appears only in the products that support it.

If you disable a model a member is using in an open conversation or session, that conversation falls back to the member's default model the next time they open it. If the member sends a message while you're making the change, they'll see an error that the model isn't available and be prompted to switch. If you lower a model's effort cap while a member has a higher level selected, their next message on that model uses the new maximum.

------------------------------------------------------------------------

## Where model access settings apply

Model access settings are enforced across these products:

[TABLE]

**Note:** Members on Claude Code CLI versions earlier than 2.1.199 still see disabled models and effort levels in the picker, but requests using them are rejected.

## Model access and Claude Code managed settings

If your organization also configures Claude Code through `managed-settings.json`, the `availableModels` setting and model access work together. In Claude Code CLI and IDE, members see only models that appear in `availableModels` *and* are enabled by their model access settings—a model removed by either one is unavailable.

Managed settings for models apply only to Claude Code CLI and IDE, not to Claude Code on web or desktop. For consistent behavior across all Claude Code surfaces, we recommend using model access settings alone. For more on managed settings, see **[Claude Code settings](../02-Claude-Code-CLI/settings.md#settings-files)**.
