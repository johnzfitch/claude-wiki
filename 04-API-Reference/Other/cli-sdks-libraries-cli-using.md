---
title: "Using the CLI - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
tags: ["api", "cli"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fcli%2Fusing)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](cli-sdks-libraries-overview.md)

ant CLI

[Quickstart](cli-sdks-libraries-cli-quickstart.md)[Authentication options](cli-sdks-libraries-cli-authentication.md)[Using the CLI](cli-sdks-libraries-cli-using.md)[Scripting and automation](cli-sdks-libraries-cli-scripting.md)[Manage resources as code](cli-sdks-libraries-cli-apply.md)[Connect to a Managed Agents session](cli-sdks-libraries-cli-sessions-connect.md)

Client SDKs

[Middleware](cli-sdks-libraries-middleware.md)[Python](cli-sdks-libraries-sdks-python.md)[TypeScript](cli-sdks-libraries-sdks-typescript.md)[C#](cli-sdks-libraries-sdks-csharp.md)[Go](cli-sdks-libraries-sdks-go.md)[Java](cli-sdks-libraries-sdks-java.md)[PHP](cli-sdks-libraries-sdks-php.md)[Ruby](cli-sdks-libraries-sdks-ruby.md)

Libraries and integrations

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

[Console](usage-limits.md)

[CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)ant CLI

# Using the CLI

Copy page



Command structure, output formats, GJSON transforms, request bodies, and debugging for the ant CLI.

Copy page



This page covers the `ant` CLI's input and output mechanics that apply across every endpoint. To install and authenticate, see the [Quickstart](cli-sdks-libraries-cli-quickstart.md). To chain commands and version-control resources, see [CLI scripting and automation](cli-sdks-libraries-cli-scripting.md).

## Command structure

Commands follow a `resource action` pattern. Nested resources use colons:

``` block
ant <resource>[:<subresource>] <action> [flags]
```



Run `ant --help` for the full resource list, or append `--help` to any subcommand for its flags.

Resources in beta (including agents, sessions, deployments, and environments) live under the `beta:` prefix. Commands in this namespace automatically send the appropriate `anthropic-beta` header for that resource, so you don't need to pass it yourself. Use `--beta <header>` only to override the default (for example, to opt into a different schema version).

```python
ant models list
ant messages create --model claude-opus-5-5 --max-tokens 1024 ...
ant beta:agents retrieve --agent-id agent_01...
ant beta:sessions:events list --session-id session_01...
```



### Global flags

| Flag                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--profile`                           | Named profile to use for this invocation (equivalent to setting `ANTHROPIC_PROFILE`). See [Switch between workspaces](cli-sdks-libraries-cli-authentication.md#switch-between-workspaces).                                                                                                                                                                                                                   |
| `--format`                            | Output format: `auto`, `json`, `jsonl`, `yaml`, `pretty`, `raw`, `explore`                                                                                                                                                                                                                                                                                                                                         |
| `--transform`                         | Filter or reshape the response with a [GJSON path](#transform-output-with-gjson)                                                                                                                                                                                                                                                                                                                                   |
| `-r`, `--raw-output`                  | Print string results without surrounding quotes, like `jq -r`                                                                                                                                                                                                                                                                                                                                                      |
| `--base-url`                          | Override the API base URL                                                                                                                                                                                                                                                                                                                                                                                          |
| `--workspace-id`                      | Optional. Workspace ID (`wrkspc_...`) to send as the `anthropic-workspace-id` header, for API keys with access to multiple workspaces (equivalent to setting `ANTHROPIC_WORKSPACE_ID`). See [Select a workspace](manage-claude-authentication.md#select-a-workspace). [Admin API](manage-claude-admin-api.md) commands take their own `--workspace-id`, which names the workspace they manage instead. |
| `--debug`                             | Print full HTTP request and response to stderr                                                                                                                                                                                                                                                                                                                                                                     |
| `--format-error`, `--transform-error` | Same as `--format` and `--transform` but applied to [error responses](cli-sdks-libraries-cli-scripting.md#inspect-errors)                                                                                                                                                                                                                                                                                    |

## Output formats

`auto` pretty-prints JSON and is the default for commands that create or modify resources. List and retrieve commands default to the [interactive explorer](#interactive-explorer) when writing to a terminal, and to pretty-printed JSON when piped. Override either default with `--format`:

```python
ant models retrieve --model-id claude-opus-5-5 --format yaml
```



Output



```python
type: model
id: claude-opus-5-5
display_name: Claude Opus 5.5
created_at: "2026-09-22T00:00:00Z"
...
```

List endpoints auto-paginate. In the default formats each item is written separately (one compact JSON object per line in `jsonl` mode, a stream of YAML documents in `yaml` mode), which streams cleanly into `head`, `grep`, and `--transform` filters.

### Interactive explorer

The explorer is a fold-and-search TUI for browsing large responses. Arrow keys expand and collapse nodes, `/` searches, `q` exits. List and retrieve commands open it by default when connected to a terminal. Pass `--format explore` to open it explicitly:

```python
ant models list --format explore
```



## Transform output with GJSON

Use `--transform` to reshape responses before printing. The expression is a [GJSON path](https://github.com/tidwall/gjson/blob/master/SYNTAX.md). For list endpoints the transform runs against each item individually, not the envelope:

```python
ant beta:agents list \
  --transform "{id,name,model}" \
  --format jsonl
```



Output



```python
{"id": "agent_011CYm1BLqPX...", "name": "Docs CLI Test Agent", "model": "claude-opus-5-5"}
{"id": "agent_011CYkVwfaEt...", "name": "Coffee Making Assistant", "model": "claude-opus-5-5"}
{"id": "agent_011CYixHhtUP...", "name": "Coding Assistant", "model": "claude-opus-5-5"}
```

### Extract a scalar

To capture a single field as an unquoted string (for example, the ID of a newly created resource), pair `--transform` with `--raw-output`. The result prints without JSON quotes and is ready to assign to a shell variable:

```python
AGENT_ID=$(ant beta:agents create \
  --name "My Agent" \
  --model '{id: claude-opus-5-5}' \
  --transform id --raw-output)

printf '%s\n' "$AGENT_ID"
```



Output



``` block
agent_011CYm1BLqPXpQRk5khsSXrs
```



`--raw-output` is distinct from `--format raw`. `--raw-output` strips JSON quotes from string results, like `jq -r`. `--format raw` prints the response body's raw JSON bytes without auto-paginating; on list endpoints it applies `--transform` to the pagination envelope rather than to each item.

## Passing request bodies

The right input mechanism depends on the shape of the data: use **flags** for scalar fields and short structured values, pipe a **stdin** document for nested or multiline bodies, and use **`@file` references** to pull file contents into any string or binary field.

### Flags

Scalar fields map directly to flags. Structured fields accept a relaxed YAML-like syntax (unquoted keys, optional quotes around strings) or strict JSON:

```python
ant beta:sessions create \
  --agent '{type: agent, id: agent_011CYm1BLqPXpQRk5khsSXrs, version: 1}' \
  --environment-id env_01595EKxaaTTGwwY3kyXdtbs \
  --title "CLI docs test session"
```



Repeatable flags build arrays. Each `--tool` or `--event` appends one element:

```python
ant beta:agents create \
  --name "Research Agent" \
  --model '{id: claude-opus-5-5}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: custom, name: search_docs, input_schema: {type: object, properties: {query: {type: string}}}}'
```



### Stdin

Pipe a JSON or YAML document to stdin to supply the full request body. Fields from stdin are merged with flags, with flags taking precedence. Here `version` is the optimistic-locking token returned by an earlier `retrieve`, and `$AGENT_ID` was captured as in [Extract a scalar](#extract-a-scalar):

```python
echo '{"description": "Updated test agent.", "version": 1}' | \
  ant beta:agents update --agent-id "$AGENT_ID"
```



Heredocs work the same way and are convenient for multiline YAML. Quote the delimiter (as in `<<'YAML'`) to disable variable expansion inside the body.

```python
ant beta:agents create <<'YAML'
name: Research Agent
model: claude-opus-5-5
system: |
  You are a research assistant. Cite sources for every claim.
tools:
  - type: agent_toolset_20260401
YAML
```



### File references

Flags that take a file path, such as `--file` on the upload command, accept a bare path:

```python
ant files upload --file ./report.pdf
```



To inline a file's contents into a string-valued field, prefix the path with `@`:

```python
ant beta:agents create \
  --name "Researcher" --model '{id: claude-opus-5-5}' \
  --system @./prompts/researcher.txt
```



Inside structured flag values, wrap the path in quotes. To send a PDF to the Messages API:

```python
ant messages create \
  --model claude-opus-5-5 \
  --max-tokens 1024 \
  --message '{role: user, content: [
    {type: document, source: {type: base64, media_type: application/pdf, data: "@./scan.pdf"}},
    {type: text, text: "Extract the text from this scanned document."}
  ]}' \
  --transform 'content.#(type=="text").text' --raw-output
```



The CLI detects the file type and encodes binary files as base64 automatically. To force a specific encoding use `@file://` for plain text or `@data://` for base64. Escape a literal leading `@` with a backslash (`\@username`).

## Debugging

Add `--debug` to any command to print the exact HTTP request and response (headers and body) to stderr. API keys are redacted.

```python
ant --debug beta:agents list
```



Output



```python
GET /v1/agents?beta=true HTTP/1.1
Host: api.anthropic.com
Anthropic-Beta: managed-agents-2026-04-01
Anthropic-Version: 2023-06-01
X-Api-Key: <REDACTED>
...
```

## Available resources

Every API resource the CLI exposes is documented in the [API reference](../Endpoints/cli-messages-create.md). For a local listing, run `ant --help`, and append `--help` to any subcommand for its flags and parameters.

## Next steps



[CLI scripting and automation](cli-sdks-libraries-cli-scripting.md)

Version-control API resources, scripting patterns, and use from Claude Code



[API reference](../Endpoints/cli-messages-create.md)

Endpoint-specific parameters, request fields, and response schemas



[CLI authentication options](cli-sdks-libraries-cli-authentication.md)

API keys, headless hosts, multiple workspaces, and named profiles
