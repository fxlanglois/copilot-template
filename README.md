# GitHub Copilot project template

A reusable starting point for projects that use GitHub Copilot in VS Code. It keeps workspace instructions and optional customization points together, so they can be copied into a new repository and adapted to that project's stack.

## What's included

```text
.github/
  agents/
    nfl-scores.agent.md       # Example of a focused custom agent
  instructions/               # Add file-specific *.instructions.md rules
  prompts/                    # Add reusable *.prompt.md tasks
  skills/                     # Add on-demand skills in <name>/SKILL.md
  copilot-instructions.md     # Workspace-wide baseline
.vscode/
  README.md                   # MCP setup notes
weekly-scores/                # Example output used by the NFL scores agent
```

The NFL scores agent and its report folder are examples from this template, not requirements for projects that use it. Keep, adapt, or remove them when creating a project.

## Use this template

1. Create a repository from this template, or copy the files and folders into an existing repository.
2. Update `.github/copilot-instructions.md` with the project's language, architecture, build, and test conventions.
3. Add focused agents, prompts, skills, or file-specific instructions only when they help with recurring work. See the README files in their folders for the expected file locations.
4. Add project-specific MCP server configuration only when needed. See `.vscode/README.md`.
5. Review the included example agent and remove it if NFL score reports are not useful to the project.

## Copilot tools and MCP

Copilot's available tools depend on the VS Code version, extensions, and the active agent. Custom agents can limit their tools in the agent frontmatter; common built-in aliases include `read`, `search`, `edit`, `execute`, `agent`, `web`, and `todo`. Use the smallest set that lets an agent do its job. Do not assume every tool is available in every environment.

MCP servers extend Copilot with external capabilities. This template intentionally does not select or configure a server: choose servers that suit each project and document any required setup. Never commit API keys, passwords, or other credentials.

## Customization locations

| What | Location |
| --- | --- |
| Workspace-wide guidance | `.github/copilot-instructions.md` |
| File-specific instructions | `.github/instructions/*.instructions.md` |
| Custom agents | `.github/agents/*.agent.md` |
| Reusable prompts | `.github/prompts/*.prompt.md` |
| On-demand skills | `.github/skills/<name>/SKILL.md` |
| VS Code MCP configuration | `.vscode/mcp.json` (optional; see `.vscode/README.md`) |

For current VS Code behavior and supported frontmatter, refer to the official [Copilot customization documentation](https://code.visualstudio.com/docs/copilot/customization/overview).
