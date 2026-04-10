# Knowledgebase Consolidation Map

Root: `/home/zack/claude-binary/mcp`

This file is a first-pass consolidation blueprint for turning the archive into a smaller MCP knowledgebase.

## Summary

- Source documents considered: **348**
- Multi-document merge families: **93**
- Documents already groupable into merge families: **290**
- Singleton documents after family grouping: **58**
- Proposed chapter-level synthesis targets: **12**
- First-pass reduction target: **105 KB docs** from **348 source docs**

## Stage 1

Merge mirrored, versioned, or directly overlapping source documents into canonical KB targets.

### Specification Families

#### `kb/spec/architecture.md`

- Family: **Architecture**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-architecture-model-context-protocol-698a3d4e78.md`
  - `spec-2025-03-26-architecture-model-context-protocol-0ff431a536.md`
  - `spec-2025-06-18-architecture-model-context-protocol-6a01ecb9df.md`
  - `spec-2025-11-25-architecture-model-context-protocol-d4b8988f42.md`
  - `spec-draft-architecture-model-context-protocol-00315b3bf0.md`

#### `kb/spec/architecture-index.md`

- Family: **Architecture Index**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-architecture-index-22bcc02a45.md`
  - `specification-2025-11-25-architecture-index-ca490ba170.md`

#### `kb/spec/authorization.md`

- Family: **Authorization**
- Source count: **4**
- Source docs:
  - `spec-2025-03-26-authorization-model-context-protocol-8bba414c28.md`
  - `spec-2025-06-18-authorization-model-context-protocol-d2811bcffa.md`
  - `spec-2025-11-25-authorization-model-context-protocol-51483c7a03.md`
  - `spec-draft-authorization-model-context-protocol-317248cc5d.md`

#### `kb/spec/basic-authorization.md`

- Family: **Basic Authorization**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-authorization-0720c28a70.md`
  - `specification-2025-11-25-basic-authorization-792922958f.md`

#### `kb/spec/basic-index.md`

- Family: **Basic Index**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-index-0d160a3428.md`
  - `specification-2025-11-25-basic-index-3c29151a2a.md`

#### `kb/spec/basic-lifecycle.md`

- Family: **Basic Lifecycle**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-lifecycle-2533ad9bfe.md`
  - `specification-2025-11-25-basic-lifecycle-4dbbc4eda7.md`

#### `kb/spec/basic-security-best-practices.md`

- Family: **Basic Security Best Practices**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-security-best-practices-ce439b6c52.md`
  - `specification-2025-11-25-basic-security-best-practices-20e822ab43.md`

#### `kb/spec/basic-transports.md`

- Family: **Basic Transports**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-transports-7a84d74f69.md`
  - `specification-2025-11-25-basic-transports-0afd336c43.md`

#### `kb/spec/basic-utilities-cancellation.md`

- Family: **Basic Utilities Cancellation**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-utilities-cancellation-5da9244220.md`
  - `specification-2025-11-25-basic-utilities-cancellation-16f5360cac.md`

#### `kb/spec/basic-utilities-ping.md`

- Family: **Basic Utilities Ping**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-utilities-ping-be5090275b.md`
  - `specification-2025-11-25-basic-utilities-ping-01fdd1e12a.md`

#### `kb/spec/basic-utilities-progress.md`

- Family: **Basic Utilities Progress**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-utilities-progress-37dd60e004.md`
  - `specification-2025-11-25-basic-utilities-progress-c1e21023fe.md`

#### `kb/spec/basic-utilities-tasks.md`

- Family: **Basic Utilities Tasks**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-basic-utilities-tasks-9551a8682e.md`
  - `specification-2025-11-25-basic-utilities-tasks-4985d95262.md`

#### `kb/spec/cancellation.md`

- Family: **Cancellation**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-cancellation-model-context-protocol-be459a7456.md`
  - `spec-2025-03-26-cancellation-model-context-protocol-8e834bae9a.md`
  - `spec-2025-06-18-cancellation-model-context-protocol-7b0b5dbe0b.md`
  - `spec-2025-11-25-cancellation-model-context-protocol-0f73210bd1.md`
  - `spec-draft-cancellation-model-context-protocol-516eb0bd5b.md`

#### `kb/spec/changelog.md`

- Family: **Changelog**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-changelog-f4ff1f23da.md`
  - `specification-2025-11-25-changelog-7c1d07e94c.md`

#### `kb/spec/client-elicitation.md`

- Family: **Client Elicitation**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-client-elicitation-9633939f6b.md`
  - `specification-2025-11-25-client-elicitation-69c839c6c9.md`

#### `kb/spec/client-roots.md`

- Family: **Client Roots**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-client-roots-d831904a69.md`
  - `specification-2025-11-25-client-roots-28660f4b0e.md`

#### `kb/spec/client-sampling.md`

- Family: **Client Sampling**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-client-sampling-d9cdb13cf8.md`
  - `specification-2025-11-25-client-sampling-bf79a2c2fd.md`

#### `kb/spec/completion.md`

- Family: **Completion**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-completion-model-context-protocol-9a88ffae71.md`
  - `spec-2025-03-26-completion-model-context-protocol-a864fab30d.md`
  - `spec-2025-06-18-completion-model-context-protocol-68b8a280d8.md`
  - `spec-2025-11-25-completion-model-context-protocol-7d7ed46294.md`
  - `spec-draft-completion-model-context-protocol-67e4125b02.md`

#### `kb/spec/elicitation.md`

- Family: **Elicitation**
- Source count: **3**
- Source docs:
  - `spec-2025-06-18-elicitation-model-context-protocol-1a6dbc0e58.md`
  - `spec-2025-11-25-elicitation-model-context-protocol-240d42349a.md`
  - `spec-draft-elicitation-model-context-protocol-913092ca56.md`

#### `kb/spec/index.md`

- Family: **Index**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-index-84ed5ef52a.md`
  - `specification-2025-11-25-index-ce7dbac411.md`

#### `kb/spec/key-changes.md`

- Family: **Key Changes / Changelog**
- Source count: **4**
- Source docs:
  - `spec-2025-03-26-key-changes-model-context-protocol-a77d8f6396.md`
  - `spec-2025-06-18-key-changes-model-context-protocol-7d9960c93c.md`
  - `spec-2025-11-25-key-changes-model-context-protocol-22e7d71eef.md`
  - `spec-draft-key-changes-model-context-protocol-17b2e6ab73.md`

#### `kb/spec/lifecycle.md`

- Family: **Lifecycle**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-lifecycle-model-context-protocol-66e0dddff6.md`
  - `spec-2025-03-26-lifecycle-model-context-protocol-eb0de97205.md`
  - `spec-2025-06-18-lifecycle-model-context-protocol-892bd888c5.md`
  - `spec-2025-11-25-lifecycle-model-context-protocol-44399078c5.md`
  - `spec-draft-lifecycle-model-context-protocol-0d133eb553.md`

#### `kb/spec/logging.md`

- Family: **Logging**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-logging-model-context-protocol-09ee2844a0.md`
  - `spec-2025-03-26-logging-model-context-protocol-f50a110998.md`
  - `spec-2025-06-18-logging-model-context-protocol-47eb5222a0.md`
  - `spec-2025-11-25-logging-model-context-protocol-037c748497.md`
  - `spec-draft-logging-model-context-protocol-3321bf4efb.md`

#### `kb/spec/overview.md`

- Family: **Overview**
- Source count: **10**
- Source docs:
  - `spec-2024-11-05-overview-model-context-protocol-cc4b143b7c.md`
  - `spec-2024-11-05-overview-model-context-protocol-ffc42d07e2.md`
  - `spec-2025-03-26-overview-model-context-protocol-83f3fc7ce3.md`
  - `spec-2025-03-26-overview-model-context-protocol-c67813c332.md`
  - `spec-2025-06-18-overview-model-context-protocol-015d42b584.md`
  - `spec-2025-06-18-overview-model-context-protocol-779945fda8.md`
  - `spec-2025-11-25-overview-model-context-protocol-229c8dde06.md`
  - `spec-2025-11-25-overview-model-context-protocol-4c03f72be1.md`
  - `spec-draft-overview-model-context-protocol-4963d5f591.md`
  - `spec-draft-overview-model-context-protocol-59bca8719f.md`

#### `kb/spec/pagination.md`

- Family: **Pagination**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-pagination-model-context-protocol-b93fc495fb.md`
  - `spec-2025-03-26-pagination-model-context-protocol-31caa69e7f.md`
  - `spec-2025-06-18-pagination-model-context-protocol-07fe2dd6e0.md`
  - `spec-2025-11-25-pagination-model-context-protocol-8383b0301a.md`
  - `spec-draft-pagination-model-context-protocol-10d20ae83e.md`

#### `kb/spec/ping.md`

- Family: **Ping**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-ping-model-context-protocol-0efd18ed1c.md`
  - `spec-2025-03-26-ping-model-context-protocol-e8ea3c39ac.md`
  - `spec-2025-06-18-ping-model-context-protocol-92c85392aa.md`
  - `spec-2025-11-25-ping-model-context-protocol-b42d51b5e6.md`
  - `spec-draft-ping-model-context-protocol-92101f910c.md`

#### `kb/spec/progress.md`

- Family: **Progress**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-progress-model-context-protocol-657512b8dd.md`
  - `spec-2025-03-26-progress-model-context-protocol-45a95a91bc.md`
  - `spec-2025-06-18-progress-model-context-protocol-8accf320fb.md`
  - `spec-2025-11-25-progress-model-context-protocol-41a8d3d481.md`
  - `spec-draft-progress-model-context-protocol-4a6c8fd9ef.md`

#### `kb/spec/prompts.md`

- Family: **Prompts**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-prompts-model-context-protocol-f3fdd22498.md`
  - `spec-2025-03-26-prompts-model-context-protocol-634f7975b6.md`
  - `spec-2025-06-18-prompts-model-context-protocol-1f910fca1d.md`
  - `spec-2025-11-25-prompts-model-context-protocol-5766ca3002.md`
  - `spec-draft-prompts-model-context-protocol-97703a979b.md`

#### `kb/spec/resources.md`

- Family: **Resources**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-resources-model-context-protocol-5bfbb5d620.md`
  - `spec-2025-03-26-resources-model-context-protocol-68412e0cca.md`
  - `spec-2025-06-18-resources-model-context-protocol-fd67269f96.md`
  - `spec-2025-11-25-resources-model-context-protocol-0327381847.md`
  - `spec-draft-resources-model-context-protocol-6df9acef1e.md`

#### `kb/spec/roots.md`

- Family: **Roots**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-roots-model-context-protocol-4abbc08cbc.md`
  - `spec-2025-03-26-roots-model-context-protocol-53e26908e5.md`
  - `spec-2025-06-18-roots-model-context-protocol-2953700c3e.md`
  - `spec-2025-11-25-roots-model-context-protocol-fc2c002988.md`
  - `spec-draft-roots-model-context-protocol-0d5b5f6c5a.md`

#### `kb/spec/sampling.md`

- Family: **Sampling**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-sampling-model-context-protocol-72607b1637.md`
  - `spec-2025-03-26-sampling-model-context-protocol-cc59fd7354.md`
  - `spec-2025-06-18-sampling-model-context-protocol-9219341c3e.md`
  - `spec-2025-11-25-sampling-model-context-protocol-b226fc8497.md`
  - `spec-draft-sampling-model-context-protocol-ca7ee709e4.md`

#### `kb/spec/schema-reference.md`

- Family: **Schema Reference**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-schema-40981d21f9.md`
  - `specification-2025-11-25-schema-b5d804e697.md`

#### `kb/spec/schema-reference.md`

- Family: **Schema Reference**
- Source count: **3**
- Source docs:
  - `spec-2025-06-18-schema-reference-model-context-protocol-9908b1e5c5.md`
  - `spec-2025-11-25-schema-reference-model-context-protocol-5775c700f0.md`
  - `spec-draft-schema-reference-model-context-protocol-5854077b12.md`

#### `kb/spec/server-index.md`

- Family: **Server Index**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-index-6718f8208b.md`
  - `specification-2025-11-25-server-index-fbec7dcd8a.md`

#### `kb/spec/server-prompts.md`

- Family: **Server Prompts**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-prompts-3605b37b57.md`
  - `specification-2025-11-25-server-prompts-ab430c85bd.md`

#### `kb/spec/server-resources.md`

- Family: **Server Resources**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-resources-450b1bc0a2.md`
  - `specification-2025-11-25-server-resources-cfcddf7e75.md`

#### `kb/spec/server-tools.md`

- Family: **Server Tools**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-tools-23fa36f860.md`
  - `specification-2025-11-25-server-tools-b4ca097afd.md`

#### `kb/spec/server-utilities-completion.md`

- Family: **Server Utilities Completion**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-utilities-completion-1644ab44fe.md`
  - `specification-2025-11-25-server-utilities-completion-3b98917a11.md`

#### `kb/spec/server-utilities-logging.md`

- Family: **Server Utilities Logging**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-utilities-logging-eba42d7f2a.md`
  - `specification-2025-11-25-server-utilities-logging-1952c8e728.md`

#### `kb/spec/server-utilities-pagination.md`

- Family: **Server Utilities Pagination**
- Source count: **2**
- Source docs:
  - `mcp-specification-2025-11-25-server-utilities-pagination-0078c6914c.md`
  - `specification-2025-11-25-server-utilities-pagination-5663b38ac4.md`

#### `kb/spec/specification-index.md`

- Family: **Specification Index**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-specification-model-context-protocol-635c22aec3.md`
  - `spec-2025-03-26-specification-model-context-protocol-483acccb3d.md`
  - `spec-2025-06-18-specification-model-context-protocol-296289fe91.md`
  - `spec-2025-11-25-specification-model-context-protocol-7b138caa8e.md`
  - `spec-draft-specification-model-context-protocol-bf007d0ac9.md`

#### `kb/spec/versioning.md`

- Family: **Specification Versioning**
- Source count: **3**
- Source docs:
  - `mcp-specification-versioning-41bc8f5bd7.md`
  - `spec-versioning-versioning-model-context-protocol-a55ad56b64.md`
  - `specification-versioning-a79e606782.md`

#### `kb/spec/tasks.md`

- Family: **Tasks**
- Source count: **2**
- Source docs:
  - `spec-2025-11-25-tasks-model-context-protocol-5285ad4d2a.md`
  - `spec-draft-tasks-model-context-protocol-f4b03e3084.md`

#### `kb/spec/tools.md`

- Family: **Tools**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-tools-model-context-protocol-4df02cf0e8.md`
  - `spec-2025-03-26-tools-model-context-protocol-b658ba63f5.md`
  - `spec-2025-06-18-tools-model-context-protocol-aca6492c13.md`
  - `spec-2025-11-25-tools-model-context-protocol-bfba858067.md`
  - `spec-draft-tools-model-context-protocol-b9cb8b57df.md`

#### `kb/spec/transports.md`

- Family: **Transports**
- Source count: **5**
- Source docs:
  - `spec-2024-11-05-transports-model-context-protocol-3ed033d2d7.md`
  - `spec-2025-03-26-transports-model-context-protocol-e6010872db.md`
  - `spec-2025-06-18-transports-model-context-protocol-e4efcb5b00.md`
  - `spec-2025-11-25-transports-model-context-protocol-937fae6437.md`
  - `spec-draft-transports-model-context-protocol-407772c542.md`

### SEP Families

#### `kb/seps/sep-1024.md`

- Family: **SEP-1024 Local Server Installation Security**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1024-mcp-client-security-requirements-for-local-server-aea40e7d30.md`
  - `mcp-docs-archive-community-seps-1024-mcp-client-security-requirements-for-local-server-fca1ed23f4.md`
  - `sep-1024-mcp-client-security-requirements-for-local-server-installation-model-co-bd7f12f1ef.md`

#### `kb/seps/sep-1034.md`

- Family: **SEP-1034 Elicitation Defaults**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1034-support-default-values-for-all-primitive-types-in-71efee9948.md`
  - `mcp-docs-archive-community-seps-1034-support-default-values-for-all-primitive-types-in-51f0871272.md`
  - `sep-1034-support-default-values-for-all-primitive-types-in-elicitation-schemas-m-c2035f8565.md`

#### `kb/seps/sep-1036.md`

- Family: **SEP-1036 URL Mode Elicitation**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1036-url-mode-elicitation-for-secure-out-of-band-intera-31847446b0.md`
  - `mcp-docs-archive-community-seps-1036-url-mode-elicitation-for-secure-out-of-band-intera-de9ea1a435.md`
  - `sep-1036-url-mode-elicitation-for-secure-out-of-band-interactions-model-context-c769fbc089.md`

#### `kb/seps/sep-1046.md`

- Family: **SEP-1046 OAuth Client Credentials**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1046-support-oauth-client-credentials-flow-in-authoriza-be6888cbf6.md`
  - `mcp-docs-archive-community-seps-1046-support-oauth-client-credentials-flow-in-authoriza-6f71a16b0a.md`
  - `sep-1046-support-oauth-client-credentials-flow-in-authorization-model-context-pr-cf703567ed.md`

#### `kb/seps/sep-1302.md`

- Family: **SEP-1302 Governance Working Groups**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1302-formalize-working-groups-and-interest-groups-in-mc-fa3a046599.md`
  - `mcp-docs-archive-community-seps-1302-formalize-working-groups-and-interest-groups-in-mc-cdef0b44a1.md`
  - `sep-1302-formalize-working-groups-and-interest-groups-in-mcp-governance-model-co-64a1fb6549.md`

#### `kb/seps/sep-1303.md`

- Family: **SEP-1303 Validation Errors as Tool Errors**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1303-input-validation-errors-as-tool-execution-errors-e0ee98762e.md`
  - `mcp-docs-archive-community-seps-1303-input-validation-errors-as-tool-execution-errors-583e37d259.md`
  - `sep-1303-input-validation-errors-as-tool-execution-errors-model-context-protocol-0511d5fbe8.md`

#### `kb/seps/sep-1319.md`

- Family: **SEP-1319 Decouple Request Payload**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1319-decouple-request-payload-from-rpc-methods-definiti-0fae799fe2.md`
  - `mcp-docs-archive-community-seps-1319-decouple-request-payload-from-rpc-methods-definiti-73564125d9.md`
  - `sep-1319-decouple-request-payload-from-rpc-methods-definition-model-context-prot-ee8e7460b2.md`

#### `kb/seps/sep-1330.md`

- Family: **SEP-1330 Elicitation Enum Schema**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1330-elicitation-enum-schema-improvements-and-standards-ab055c2758.md`
  - `mcp-docs-archive-community-seps-1330-elicitation-enum-schema-improvements-and-standards-99952cca75.md`
  - `sep-1330-elicitation-enum-schema-improvements-and-standards-compliance-model-con-7baec4b4a1.md`

#### `kb/seps/sep-1577.md`

- Family: **SEP-1577 Sampling With Tools**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1577-sampling-with-tools-cc3c6b896d.md`
  - `mcp-docs-archive-community-seps-1577-sampling-with-tools-9bf9fe6bb8.md`
  - `sep-1577-sampling-with-tools-model-context-protocol-9c86a91fc3.md`

#### `kb/seps/sep-1613.md`

- Family: **SEP-1613 JSON Schema 2020-12**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1613-establish-json-schema-2020-12-as-default-dialect-f-35b1c68c1d.md`
  - `mcp-docs-archive-community-seps-1613-establish-json-schema-2020-12-as-default-dialect-f-80f4bafdc5.md`
  - `sep-1613-establish-json-schema-2020-12-as-default-dialect-for-mcp-model-context-eb3d817d3d.md`

#### `kb/seps/sep-1686.md`

- Family: **SEP-1686 Tasks**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1686-tasks-b7fc415839.md`
  - `mcp-docs-archive-community-seps-1686-tasks-2dba59b418.md`
  - `sep-1686-tasks-model-context-protocol-b7c948f47f.md`

#### `kb/seps/sep-1699.md`

- Family: **SEP-1699 SSE Polling via Disconnect**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1699-support-sse-polling-via-server-side-disconnect-867a6c9367.md`
  - `mcp-docs-archive-community-seps-1699-support-sse-polling-via-server-side-disconnect-6557e471d3.md`
  - `sep-1699-support-sse-polling-via-server-side-disconnect-model-context-protocol-3bcd4a41f6.md`

#### `kb/seps/sep-1730.md`

- Family: **SEP-1730 SDK Tiering**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1730-sdks-tiering-system-e7b24091c5.md`
  - `mcp-docs-archive-community-seps-1730-sdks-tiering-system-a6b00c2ff1.md`
  - `sep-1730-sdks-tiering-system-model-context-protocol-23c572b7d1.md`

#### `kb/seps/sep-1850.md`

- Family: **SEP-1850 PR-Based SEP Workflow**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1850-pr-based-sep-workflow-b57ba9e78d.md`
  - `mcp-docs-archive-community-seps-1850-pr-based-sep-workflow-e3c6379b7a.md`
  - `sep-1850-pr-based-sep-workflow-model-context-protocol-25c7b50ec1.md`

#### `kb/seps/sep-1865.md`

- Family: **SEP-1865 MCP Apps**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-1865-mcp-apps-interactive-user-interfaces-for-mcp-40a09e7a5d.md`
  - `mcp-docs-archive-community-seps-1865-mcp-apps-interactive-user-interfaces-for-mcp-32bb21eb9c.md`
  - `sep-1865-mcp-apps-interactive-user-interfaces-for-mcp-model-context-protocol-14073dde1b.md`

#### `kb/seps/sep-2085.md`

- Family: **SEP-2085 Governance Succession**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-2085-governance-succession-and-amendment-6f948341b0.md`
  - `mcp-docs-archive-community-seps-2085-governance-succession-and-amendment-a71f7df6a4.md`
  - `sep-2085-governance-succession-and-amendment-procedures-model-context-protocol-5a0b0efc4e.md`

#### `kb/seps/sep-2133.md`

- Family: **SEP-2133 Extensions**
- Source count: **3**
- Source docs:
  - `mcp-docs-archive-community-seps-2133-extensions-a1ac1f4e52.md`
  - `mcp-ext-2133-extensions-84c1e161cf.md`
  - `sep-2133-extensions-model-context-protocol-b3d37db54b.md`

#### `kb/seps/sep-932.md`

- Family: **SEP-932 MCP Governance**
- Source count: **3**
- Source docs:
  - `mcp-docs-archive-community-seps-932-model-context-protocol-governance-eb8202fc6a.md`
  - `mcp-ext-932-model-context-protocol-governance-24360b3e60.md`
  - `sep-932-model-context-protocol-governance-model-context-protocol-9c20ee4d1f.md`

#### `kb/seps/sep-973.md`

- Family: **SEP-973 Additional Metadata**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-973-expose-additional-metadata-for-implementations-res-a8a1c88257.md`
  - `mcp-docs-archive-community-seps-973-expose-additional-metadata-for-implementations-res-f87d5c8b24.md`
  - `sep-973-expose-additional-metadata-for-implementations-resources-tools-and-promp-16d4e286be.md`

#### `kb/seps/sep-985.md`

- Family: **SEP-985 Protected Resource Metadata**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-985-align-oauth-20-protected-resource-metadata-with-rf-eec9feb130.md`
  - `mcp-docs-archive-community-seps-985-align-oauth-20-protected-resource-metadata-with-rf-19f6aaf406.md`
  - `sep-985-align-oauth-2-0-protected-resource-metadata-with-rfc-9728-model-context-a7d372ab65.md`

#### `kb/seps/sep-986.md`

- Family: **SEP-986 Tool Name Format**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-986-specify-format-for-tool-names-6397a5e80d.md`
  - `mcp-docs-archive-community-seps-986-specify-format-for-tool-names-30aab22c8c.md`
  - `sep-986-specify-format-for-tool-names-model-context-protocol-3cc71bd8ff.md`

#### `kb/seps/sep-990.md`

- Family: **SEP-990 Enterprise IdP Controls**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-990-enable-enterprise-idp-policy-controls-during-mcp-o-7fab43015b.md`
  - `mcp-docs-archive-community-seps-990-enable-enterprise-idp-policy-controls-during-mcp-o-b8122a6cdb.md`
  - `sep-990-enable-enterprise-idp-policy-controls-during-mcp-oauth-flows-model-conte-04b1e7877c.md`

#### `kb/seps/sep-991.md`

- Family: **SEP-991 URL-Based Client Registration**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-991-enable-url-based-client-registration-using-oauth-c-e28a8c39da.md`
  - `mcp-docs-archive-community-seps-991-enable-url-based-client-registration-using-oauth-c-f36e7d9569.md`
  - `sep-991-enable-url-based-client-registration-using-oauth-client-id-metadata-docu-63243fee3b.md`

#### `kb/seps/sep-994.md`

- Family: **SEP-994 Shared Communication Practices**
- Source count: **3**
- Source docs:
  - `mcp-community-seps-994-shared-communication-practicesguidelines-ec20082e56.md`
  - `mcp-docs-archive-community-seps-994-shared-communication-practicesguidelines-a3b6002f70.md`
  - `sep-994-shared-communication-practices-guidelines-model-context-protocol-d2179ace80.md`

### Registry Families

#### `kb/registry/publish-quickstart.md`

- Family: **Publish Quickstart**
- Source count: **3**
- Source docs:
  - `mcp-registry-quickstart-e6ff5eed5e.md`
  - `quickstart-publish-an-mcp-server-to-the-mcp-registry-model-context-protocol-da7c547f0a.md`
  - `registry-quickstart-3f105fc718.md`

#### `kb/registry/versioning.md`

- Family: **Published Server Versioning**
- Source count: **3**
- Source docs:
  - `mcp-registry-versioning-6fcc0a6ac0.md`
  - `registry-versioning-ee31cd16b4.md`
  - `versioning-published-mcp-servers-model-context-protocol-8af99f43a1.md`

#### `kb/registry/publishing-authentication.md`

- Family: **Publishing Authentication**
- Source count: **3**
- Source docs:
  - `how-to-authenticate-when-publishing-to-the-official-mcp-registry-model-context-p-bb2ed5c037.md`
  - `mcp-registry-authentication-2069fafb27.md`
  - `registry-authentication-73a78f7ec2.md`

#### `kb/registry/publishing-github-actions.md`

- Family: **Publishing with GitHub Actions**
- Source count: **3**
- Source docs:
  - `how-to-automate-publishing-with-github-actions-model-context-protocol-a52528320d.md`
  - `mcp-registry-github-actions-68e27685c0.md`
  - `registry-github-actions-6a1b4b80bd.md`

#### `kb/registry/aggregators.md`

- Family: **Registry Aggregators**
- Source count: **3**
- Source docs:
  - `mcp-registry-aggregators-model-context-protocol-aafdce715d.md`
  - `mcp-registry-registry-aggregators-6621b4f2f4.md`
  - `registry-registry-aggregators-0bbd5653b8.md`

#### `kb/registry/faq.md`

- Family: **Registry FAQ**
- Source count: **3**
- Source docs:
  - `frequently-asked-questions-model-context-protocol-b550e3fbd4.md`
  - `mcp-registry-faq-84073d2a31.md`
  - `registry-faq-12a537c322.md`

#### `kb/registry/moderation-policy.md`

- Family: **Registry Moderation Policy**
- Source count: **3**
- Source docs:
  - `mcp-registry-moderation-policy-b722cab53f.md`
  - `registry-moderation-policy-0e93cd74cb.md`
  - `the-mcp-registry-moderation-policy-model-context-protocol-aba873f691.md`

#### `kb/registry/overview.md`

- Family: **Registry Overview**
- Source count: **3**
- Source docs:
  - `mcp-registry-about-37243162c9.md`
  - `registry-about-4b88194089.md`
  - `the-mcp-registry-model-context-protocol-31b411648a.md`

#### `kb/registry/terms-of-service.md`

- Family: **Registry Terms of Service**
- Source count: **3**
- Source docs:
  - `mcp-registry-terms-of-service-581341b7df.md`
  - `official-mcp-registry-terms-of-service-model-context-protocol-e8e36fe44f.md`
  - `registry-terms-of-service-679ab4c57e.md`

#### `kb/registry/remote-servers.md`

- Family: **Remote Servers**
- Source count: **3**
- Source docs:
  - `mcp-registry-remote-servers-71f1e45da8.md`
  - `publishing-remote-servers-model-context-protocol-b74860e8b4.md`
  - `registry-remote-servers-39688c5212.md`

#### `kb/registry/package-types.md`

- Family: **Supported Package Types**
- Source count: **3**
- Source docs:
  - `mcp-registry-package-types-00aa1d4d33.md`
  - `mcp-registry-supported-package-types-model-context-protocol-099c385b0e.md`
  - `registry-package-types-f6f1740120.md`

### Anthropic Directory Families

#### `kb/anthropic/directory-policy.md`

- Family: **Anthropic Directory Policy**
- Source count: **2**
- Source docs:
  - `anthropic-mcp-directory-policy-80079212dc.md`
  - `anthropic-mcp-directory-policy-d8b6216098.md`

#### `kb/anthropic/directory-terms.md`

- Family: **Anthropic Directory Terms**
- Source count: **2**
- Source docs:
  - `anthropic-mcp-directory-terms-and-conditions-2d3597ea94.md`
  - `anthropic-mcp-directory-terms-and-conditions-f6dae27aeb.md`

### Connector and Integration Families

#### `kb/integrations/custom-remote-connectors.md`

- Family: **Custom Remote Connector Getting Started**
- Source count: **4**
- Source docs:
  - `about-integrations-using-remote-mcp-978ed1d4e8.md`
  - `get-started-with-custom-connectors-using-remote-mcp-dcba133490.md`
  - `getting-started-with-custom-connectors-using-remote-mcp-0e4d1345e1.md`
  - `getting-started-with-custom-connectors-using-remote-mcp-74392cf540.md`

### Extension Families

#### `kb/extensions/mcp-apps.md`

- Family: **MCP Apps Overview**
- Source count: **3**
- Source docs:
  - `mcp-apps-model-context-protocol-e654443dd1.md`
  - `mcp-docs-archive-docs-extensions-apps-481f95fb07.md`
  - `mcp-ext-extensions-apps-7733b41c6d.md`

### SDK Families

#### `kb/sdk/overview.md`

- Family: **SDK Overview**
- Source count: **3**
- Source docs:
  - `mcp-docs-archive-docs-sdk-2187d95d65.md`
  - `mcp-docs-sdk-063fe03275.md`
  - `sdks-model-context-protocol-6f28854504.md`

### Tooling Families

#### `kb/tools/inspector.md`

- Family: **MCP Inspector**
- Source count: **3**
- Source docs:
  - `mcp-docs-archive-docs-tools-inspector-75c54000e4.md`
  - `mcp-docs-tools-inspector-f6f8a2d1c5.md`
  - `mcp-inspector-model-context-protocol-7fb233a187.md`

### Authorization Families

#### `kb/security/understanding-authorization.md`

- Family: **Understanding Authorization**
- Source count: **3**
- Source docs:
  - `mcp-docs-archive-docs-tutorials-security-authorization-a02cb4a918.md`
  - `mcp-docs-tutorials-security-authorization-409c957cd5.md`
  - `understanding-authorization-in-mcp-model-context-protocol-5e9bbaa2fc.md`

### Example Families

#### `kb/examples/clients.md`

- Family: **Example Clients**
- Source count: **2**
- Source docs:
  - `example-clients-model-context-protocol-ccb4d8d2eb.md`
  - `mcp-clients-32b41e53ad.md`

#### `kb/examples/servers.md`

- Family: **Example Servers**
- Source count: **2**
- Source docs:
  - `example-servers-model-context-protocol-73eece0ddf.md`
  - `mcp-examples-bfd0f65dff.md`

### Claude Code Families

#### `kb/clients/claude-code-mcp.md`

- Family: **Connect Claude Code via MCP**
- Source count: **2**
- Source docs:
  - `connect-claude-code-to-tools-via-mcp-claude-code-docs-e8ecdafbf2.md`
  - `mcp.md`

### Community Families

#### `kb/community/antitrust.md`

- Family: **Community Antitrust Policy**
- Source count: **3**
- Source docs:
  - `antitrust-policy-model-context-protocol-020d608b39.md`
  - `mcp-community-antitrust-412843dba5.md`
  - `mcp-docs-archive-community-antitrust-2f8ad50722.md`

#### `kb/community/communication.md`

- Family: **Community Communication**
- Source count: **3**
- Source docs:
  - `contributor-communication-model-context-protocol-8cf3cbe878.md`
  - `mcp-community-communication-2f08b8773c.md`
  - `mcp-docs-archive-community-communication-694143bf6b.md`

#### `kb/community/contributing.md`

- Family: **Community Contributing**
- Source count: **3**
- Source docs:
  - `contributing-to-mcp-model-context-protocol-61b33c251c.md`
  - `mcp-community-contributing-bc99a626a6.md`
  - `mcp-docs-archive-community-contributing-5086a5ef73.md`

## Stage 2

Synthesize the remaining singleton docs, plus selected Stage 1 family outputs, into broader knowledgebase chapters. Stage 2 is intentionally a second-level editorial plan, so some documents already merged in Stage 1 are referenced again here as inputs to broader chapters.

### `kb/core/foundations.md`

- Chapter: **Foundations**
- Scope: Core conceptual docs that explain what MCP is, how it is structured, and how clients and servers relate.
- Source count: **7**
- Source docs:
  - `architecture-overview-model-context-protocol-172e80d748.md`
  - `design-principles-model-context-protocol-1bc6496be0.md`
  - `understanding-mcp-clients-model-context-protocol-dc61cc26c5.md`
  - `understanding-mcp-servers-model-context-protocol-a76ca51de3.md`
  - `what-is-the-model-context-protocol-mcp-model-context-protocol-f2490090ea.md`
  - `mcp-index-f2e73dd00c.md`
  - `mcp-readme-29b3b022b5.md`

### `kb/clients/connection-and-configuration.md`

- Chapter: **Client Connection and Configuration**
- Scope: Client setup, Claude Code integration, local/remote server connection, and server configuration guidance.
- Source count: **7**
- Source docs:
  - `mcp.md`
  - `connect-claude-code-to-tools-via-mcp-claude-code-docs-e8ecdafbf2.md`
  - `connect-to-local-mcp-servers-model-context-protocol-e7260110bd.md`
  - `connect-to-remote-mcp-servers-model-context-protocol-f5df55079d.md`
  - `getting-started-with-local-mcp-servers-on-claude-desktop-3de645247d.md`
  - `mcp-server-configuration-guide.md`
  - `server-types.md`

### `kb/build/building-and-operating-mcp.md`

- Chapter: **Building and Operating MCP**
- Scope: Build guides, SDK entry points, enterprise deployment, and operational server setup.
- Source count: **9**
- Source docs:
  - `agent-sdk-mcp-91b1842bca.md`
  - `build-an-mcp-app-model-context-protocol-4c6e848874.md`
  - `build-an-mcp-client-model-context-protocol-f0c7f3a724.md`
  - `build-an-mcp-server-model-context-protocol-837f5581b7.md`
  - `building-custom-connectors-via-remote-mcp-servers-813ea92951.md`
  - `deploying-enterprise-grade-mcp-servers-with-desktop-extensions-71834ffb88.md`
  - `enterprise-managed-authorization-model-context-protocol-de621206a5.md`
  - `oauth-client-credentials-model-context-protocol-8de706439f.md`
  - `security-best-practices-model-context-protocol-0613e0768d.md`

### `kb/tools/workflows-and-tooling.md`

- Chapter: **Workflows and Tooling**
- Scope: Tool invocation patterns, hooks, custom tools, and implementation-level workflow docs.
- Source count: **9**
- Source docs:
  - `authentication.md`
  - `calculator-tool.md`
  - `crop-tool.md`
  - `custom-tools.md`
  - `extended-thinking-with-tool-use.md`
  - `mcp-docs - Automate workflows with hooks.md`
  - `mcp-docs - Hooks reference.md`
  - `tool-usage.md`
  - `tool-use-with-pydantic.md`

### `kb/extensions/extensions-and-skills.md`

- Chapter: **Extensions and Skills**
- Scope: Extensions, app-related capability docs, and agent skill material that should be synthesized together.
- Source count: **6**
- Source docs:
  - `authorization-extensions-model-context-protocol-755df47eed.md`
  - `extension-support-matrix-model-context-protocol-0aca1db202.md`
  - `extensions-overview-model-context-protocol-8a51d1e160.md`
  - `mcp-ext-ext-skills-8664e5b617.md`
  - `mcp-extensions-df06a140ba.md`
  - `skills-explained-how-skills-compares-to-prompts-projects-mcp-and-subagents-claude.md`

### `kb/governance/governance-roadmap-and-process.md`

- Chapter: **Governance, Roadmap, and Process**
- Scope: Governance structure, roadmap, working groups, and documentation process guidance.
- Source count: **5**
- Source docs:
  - `governance-and-stewardship-model-context-protocol-82b75e3325.md`
  - `roadmap-model-context-protocol-f1a3aa3683.md`
  - `sep-guidelines-model-context-protocol-b35e51bb7f.md`
  - `specification-enhancement-proposals-seps-model-context-protocol-a85e64ea31.md`
  - `working-and-interest-groups-model-context-protocol-d36a968157.md`

### `kb/research/archive-analysis.md`

- Chapter: **Archive Analysis and Verification**
- Scope: Internal archive analyses, verification logs, and reverse-engineering notes that support the knowledgebase but should stay separate from normative docs.
- Source count: **11**
- Source docs:
  - `claude-code-mcp-knowledgebase.md`
  - `claude-code-vs-grepai-analysis.md`
  - `claude-code-vs-grepai-comparison.html`
  - `mcp-agent-knowledgebase.md`
  - `mcp-complete-verification-0758f17092.md`
  - `mcp-coverage-report-d9e8757b4b.md`
  - `mcp-overview-report.md`
  - `mcp-sitemap-analysis-935c339ba2.md`
  - `mcp-verification-complete-b14fcfa45b.md`
  - `pagescope-2026-02-01.md`
  - `pyghidra-lite.md`

### `kb/registry/submission-guide.md`

- Chapter: **Registry Submission Guide**
- Scope: End-to-end submission and directory guidance that complements the registry publishing families.
- Source count: **1**
- Source docs:
  - `remote-mcp-server-submission-guide-claude-help-center-93aa8232ae.md`

### `kb/examples/reference-material.md`

- Chapter: **Reference Material**
- Scope: Specific examples and product-specific reference docs that do not currently cluster with mirrors.
- Source count: **1**
- Source docs:
  - `mcp-2.md`

### `kb/spec/open-proposals.md`

- Chapter: **Open Proposals Without Mirrors**
- Scope: Open proposal docs that currently exist as singletons and should remain standalone KB pages.
- Source count: **2**
- Source docs:
  - `sep-2260-require-server-requests-to-be-associated-with-a-client-request-model-co-b081193081.md`
  - `sep-414-document-opentelemetry-trace-context-propagation-conventions-model-conte-a9796a4ff3.md`

### `kb/spec/messages-2024-11-05.md`

- Chapter: **Historic Messages Page**
- Scope: The one-off 2024-11-05 messages page should stay as its own historical spec note.
- Source count: **1**
- Source docs:
  - `spec-2024-11-05-messages-model-context-protocol-e1f667d891.md`

### `kb/backlog/unassigned-singletons.md`

- Chapter: **Unassigned Singletons**
- Scope: Docs that still need a chapter decision after the first-pass synthesis plan.
- Source count: **1**
- Source docs:
  - `sdk-tiering-system-model-context-protocol-d5195df35e.md`

## Recommendation

1. Consolidate Stage 1 families first, because these are the safest reductions and usually involve mirrors, archived copies, or version-variant exports.
2. Build Stage 2 chapters after Stage 1, because those chapters require human editorial synthesis rather than straight merging.
3. Preserve provenance inside each KB doc by recording the source file list and any protocol version boundaries.
