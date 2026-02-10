---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/build-with-claude/files"
title: "Example: Reading a text file and sending it as plain text"
---


Capabilities
Files API
Copy page

The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the code execution tool to provide inputs (e.g. datasets and documents) and then download outputs (e.g. charts). You can also use the Files API to prevent having to continually re-upload frequently used documents and images across multiple API calls. You can explore the API reference directly, in addition to this guide.

The Files API is currently in beta. Please reach out through our feedback form to share your experience with the Files API.

Supported models

Referencing a file_id in a Messages request is supported in all models that support the given file type. For example, images are supported in all Claude 3+ models, PDFs in all Claude 3.5+ models, and various other file types for the code execution tool in Claude Haiku 4.5 plus all Claude 3.7+ models.

The Files API is currently not supported on Amazon Bedrock or Google Vertex AI.

How the Files API works

The Files API provides a simple create-once, use-many-times approach for working with files:

Upload files to our secure storage and receive a unique file_id
Download files that are created from skills or the code execution tool
Reference files in Messages requests using the file_id instead of re-uploading content
Manage your files with list, retrieve, and delete operations
How to use the Files API

To use the Files API, you'll need to include the beta feature header: anthropic-beta: files-api-2025-04-14.

Uploading a file

Upload a file to be referenced in future API calls:

Shell
curl -X POST https://api.anthropic.com/v1/files \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14" \
 -F "file=@/path/to/document.pdf"

The response from uploading a file will include:

{
 "id": "file_011CNha8iCJcU1wXNR6q4V8w",
 "type": "file",
 "filename": "document.pdf",
 "mime_type": "application/pdf",
 "size_bytes": 1024000,
 "created_at": "2025-01-01T00:00:00Z",
 "downloadable": false
}
Using a file in messages

Once uploaded, reference the file using its file_id:

Shell
curl -X POST https://api.anthropic.com/v1/messages \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14" \
 -H "content-type: application/json" \
 -d '{
 "model": "claude-sonnet-4-5",
 "max_tokens": 1024,
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "Please summarize this document for me." 
 },
 {
 "type": "document",
 "source": {
 "type": "file",
 "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
 }
 }
 ]
 }
 ]
 }'
File types and content blocks

The Files API supports different file types that correspond to different content block types:

File Type MIME Type Content Block Type Use Case
PDF application/pdf document Text analysis, document processing
Plain text text/plain document Text analysis, processing
Images image/jpeg, image/png, image/gif, image/webp image Image analysis, visual tasks
Datasets, others Varies container_upload Analyze data, create visualizations
Working with other file formats

For file types that are not supported as document blocks (.csv, .txt, .md, .docx, .xlsx), convert the files to plain text, and include the content directly in your message:

Shell
# Example: Reading a text file and sending it as plain text
# Note: For files with special characters, consider base64 encoding
TEXT_CONTENT=$(cat document.txt | jq -Rs .)

curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -d @- <<EOF
{
 "model": "claude-sonnet-4-5",
 "max_tokens": 1024,
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "Here's the document content:\n\n${TEXT_CONTENT}\n\nPlease summarize this document."
 }
 ]
 }
 ]
}
EOF

For .docx files containing images, convert them to PDF format first, then use PDF support to take advantage of the built-in image parsing. This allows using citations from the PDF document.

Document blocks

For PDFs and text files, use the document content block:

{
 "type": "document",
 "source": {
 "type": "file",
 "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
 },
 "title": "Document Title", // Optional
 "context": "Context about the document", // Optional 
 "citations": {"enabled": true} // Optional, enables citations
}
Image blocks

For images, use the image content block:

{
 "type": "image",
 "source": {
 "type": "file",
 "file_id": "file_011CPMxVD3fHLUhvTqtsQA5w"
 }
}
Managing files
List files

Retrieve a list of your uploaded files:

Shell
curl https://api.anthropic.com/v1/files \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14"
Get file metadata

Retrieve information about a specific file:

Shell
curl https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14"
Delete a file

Remove a file from your workspace:

Shell
curl -X DELETE https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14"
Downloading a file

Download files that have been created by skills or the code execution tool:

Shell
curl -X GET "https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w/content" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14" \
 --output downloaded_file.txt

You can only download files that were created by skills or the code execution tool. Files that you uploaded cannot be downloaded.

File storage and limits
Storage limits
Maximum file size: 500 MB per file
Total storage: 100 GB per organization
File lifecycle
Files are scoped to the workspace of the API key. Other API keys can use files created by any other API key associated with the same workspace
Files persist until you delete them
Deleted files cannot be recovered
Files are inaccessible via the API shortly after deletion, but they may persist in active Messages API calls and associated tool uses
Files that users delete will be deleted in accordance with our data retention policy.
Error handling

Common errors when using the Files API include:

File not found (404): The specified file_id doesn't exist or you don't have access to it
Invalid file type (400): The file type doesn't match the content block type (e.g., using an image file in a document block)
Exceeds context window size (400): The file is larger than the context window size (e.g. using a 500 MB plaintext file in a /v1/messages request)
Invalid filename (400): Filename doesn't meet the length requirements (1-255 characters) or contains forbidden characters (<, >, :, ", |, ?, *, \, /, or unicode characters 0-31)
File too large (413): File exceeds the 500 MB limit
Storage limit exceeded (403): Your organization has reached the 100 GB storage limit
{
 "type": "error",
 "error": {
 "type": "invalid_request_error",
 "message": "File not found: file_011CNha8iCJcU1wXNR6q4V8w"
 }
}
Usage and billing

File API operations are free:

Uploading files
Downloading files
Listing files
Getting file metadata
Deleting files

File content used in Messages requests are priced as input tokens. You can only download files created by skills or the code execution tool.

Rate limits

During the beta period:

File-related API calls are limited to approximately 100 requests per minute
Contact us if you need higher limits for your use case

Was this page helpful?