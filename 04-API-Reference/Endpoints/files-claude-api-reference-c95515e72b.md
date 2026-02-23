---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:22:59Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/files"
title: "Files - Claude API Reference"
---

Copy page

C#

# Files

##### [Upload File](/docs/en/api/beta/files/upload)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

[FileListPageResponse](/docs/en/api/beta#FileListPageResponse) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

[FileMetadata](/docs/en/api/beta#file_metadata) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

[DeletedFile](/docs/en/api/beta#deleted_file) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file_id}

##### ModelsExpand Collapse 

class DeletedFile:

required string ID

ID of the deleted file.

Type Type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing when the file was created.

required string Filename

Original filename of the uploaded file.

required string MimeType

MIME type of the file.

required Long SizeBytes

Size of the file in bytes.

JsonElement Type "file"constant

Object type.

For files, this is always `"file"`.

Boolean Downloadable

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
