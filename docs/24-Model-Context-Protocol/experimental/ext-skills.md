# Skills Over MCP - Experimental Extension

**Repository**: https://github.com/modelcontextprotocol/experimental-ext-skills
**Status**: Experimental / Work in Progress
**License**: Apache-2.0

## Purpose

This experimental repository serves as an incubation space for exploring how "agent skills" (structured workflow instructions) can be discovered and distributed through Model Context Protocol (MCP) primitives.

## Core Mission

The interest group investigates whether existing MCP mechanisms adequately support rich skill definitions, or if new conventions and standardization are needed for the community to align on implementation approaches.

## Key Problems Being Addressed

The group identifies several limitations with current approaches:

### 1. Static Skill Loading
Skills only load at server initialization; updates require server restart. This creates friction when:
- Skills need to be updated dynamically
- New skills become available
- Existing skills are modified or removed

### 2. Size Constraints
Complex workflows with hundreds of lines and bundled file references exceed practical instruction limits. This affects:
- Multi-step workflows
- Skills with extensive documentation
- Skills that reference multiple files or resources

### 3. Discovery Gap
No mechanism exists for users to identify available skills associated with installed MCP servers. Users cannot:
- Browse available skills before execution
- Understand skill capabilities without running them
- Search for specific skills across multiple servers

### 4. Orchestration Complexity
Skills requiring coordination across multiple MCP servers lack standardized approaches. Challenges include:
- Cross-server skill composition
- State management across servers
- Error handling in multi-server workflows
- Permission and security boundaries

## Current Status

**Work in Progress** - The repository is in active development and will eventually consolidate content from an accompanying public Google Document.

### Community Discussion Channels

Until finalized, the community continues discussions via:
- **Google Document**: Public collaboration space (linked in repository)
- **Discord**: #skills-over-mcp-ig channel

## Repository Details

- **Organization**: modelcontextprotocol
- **License**: Apache-2.0
- **Contents**: Minimal (README and LICENSE only as of current inspection)
- **Community Interest**: 3 stars, 1 fork
- **Type**: Experimental Extension (not part of official MCP specification)

## Important Notice

The project explicitly emphasizes that contents remain exploratory and **do not constitute official MCP specifications**. This is an incubation space for:
- Prototyping ideas
- Gathering community feedback
- Testing implementation approaches
- Building consensus on standardization

## Related MCP Concepts

Skills relate to existing MCP primitives:
- **Prompts**: Templated messages and workflows
- **Tools**: Functions that can be executed
- **Resources**: Context and data sources

The Skills IG explores how these primitives can be extended or augmented to support more complex, composable workflows.

## Potential Use Cases

Skills over MCP could enable:
- **Workflow Automation**: Multi-step processes that coordinate multiple tools
- **Domain-Specific Templates**: Pre-built workflows for common tasks
- **Cross-Server Orchestration**: Skills that utilize tools from multiple MCP servers
- **Dynamic Skill Loading**: Hot-reloading skills without server restart
- **Skill Discovery UI**: Browseable catalog of available skills

## Next Steps for Interested Developers

1. **Join the Discussion**: Participate in #skills-over-mcp-ig on Discord
2. **Review the Google Doc**: Check the linked collaboration document
3. **Monitor the Repository**: Watch for updates and specification drafts
4. **Provide Feedback**: Share use cases and implementation challenges
5. **Prototype**: Build experimental implementations to test ideas

## Relationship to Official MCP

This is an **experimental extension** under the governance model defined in [SEP-2133 (Extensions)](https://modelcontextprotocol.io/community/seps/2133-extensions.md).

Experimental extensions:
- Provide incubation pathway for new ideas
- Allow community collaboration before formal specification
- Enable prototyping without commitment to official support
- May eventually graduate to official extensions or core protocol

---

*Last Updated: 2026-02-02*
*Source: https://github.com/modelcontextprotocol/experimental-ext-skills*
