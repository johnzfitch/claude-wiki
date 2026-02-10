---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:07:23Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/files"
title: "Files - Claude API Reference"
---

Copy page

TypeScript

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

client.beta.files.upload(FileUploadParams { file, betas } params, RequestOptionsoptions?): [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

post/v1/files

##### [List Files](/docs/en/api/beta/files/list)

client.beta.files.list(FileListParams { after_id, before_id, limit, betas } params?, RequestOptionsoptions?): Page\<[FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more } \>

get/v1/files

##### [Download File](/docs/en/api/beta/files/download)

client.beta.files.download(stringfileID, FileDownloadParams { betas } params?, RequestOptionsoptions?): Response

get/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParams { betas } params?, RequestOptionsoptions?): [FileMetadata](/docs/en/api/beta#file_metadata) { id, created_at, filename, 4 more }

get/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

client.beta.files.delete(stringfileID, FileDeleteParams { betas } params?, RequestOptionsoptions?): [DeletedFile](/docs/en/api/beta#deleted_file) { id, type }

delete/v1/files/{file_id}

##### ModelsExpand Collapse 

DeletedFile { id, type }

id: string

ID of the deleted file.

type?: "file_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file_deleted"

FileMetadata { id, created_at, filename, 4 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created_at: string

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: string

Original filename of the uploaded file.

maxLength500

minLength1

mime_type: string

MIME type of the file.

maxLength255

minLength1

size_bytes: number

Size of the file in bytes.

minimum0

type: "file"

Object type.

For files, this is always `"file"`.

Accepts one of the following:

"file"

downloadable?: boolean

Whether the file can be downloaded.

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
