---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/api/client-sdks"
---


Using the API
Client SDKs
Copy page
We provide client libraries in a number of popular languages that make it easier to work with the Claude API.

This page includes brief installation instructions and links to the open-source GitHub repositories for Anthropic's Client SDKs. For basic usage instructions, see the API reference For detailed usage instructions, refer to each SDK's GitHub repository.

Additional configuration is needed to use Anthropic's Client SDKs through a partner platform. If you are using Amazon Bedrock, see this guide; if you are using Google Cloud Vertex AI, see this guide; if you are using Microsoft Foundry, see this guide.

Python

Python library GitHub repo

Requirements: Python 3.8+

Minimum SDK version: 0.22.0

Installation:

pip install anthropic
TypeScript

TypeScript library GitHub repo

While this library is in TypeScript, it can also be used in JavaScript libraries.

Minimum SDK version: 0.37.0

Installation:

npm install @anthropic-ai/sdk
Java

Java library GitHub repo

Requirements: Java 8 or later

Installation:

Gradle:

implementation("com.anthropic:anthropic-java:2.10.0")

Maven:

<dependency>
 <groupId>com.anthropic</groupId>
 <artifactId>anthropic-java</artifactId>
 <version>2.10.0</version>
</dependency>
Go

Go library GitHub repo

Requirements: Go 1.22+

Installation:

go get -u 'github.com/anthropics/anthropic-sdk-go@v1.17.0'
C#

C# library GitHub repo

The C# SDK is currently in beta.

Requirements: .NET 8 or later

Installation:

dotnet add package Anthropic
Ruby

Ruby library GitHub repo

Requirements: Ruby 3.2.0 or later

Installation:

Add to your Gemfile:

gem "anthropic", "~> 1.13.0"

Then run:

bundle install
PHP

PHP library GitHub repo

The PHP SDK is currently in beta.

Requirements: PHP 8.1.0 or higher

Installation:

composer require "anthropic-ai/sdk 0.3.0"
Beta namespace in client SDKs

Every SDK has a beta namespace that is available for accessing new features that Anthropic releases in beta versions. Use this in conjunction with beta headers to access these features. Refer to each SDK's GitHub repository for specific usage examples.

Was this page helpful?