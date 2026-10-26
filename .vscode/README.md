# VS Code and MCP configuration

This template does not enable any MCP servers by default. When a project needs one, configure it in `.vscode/mcp.json` using the server's official setup instructions and the VS Code MCP configuration format.

Before sharing the configuration:

- Keep credentials out of the file. Use supported environment-variable or input-variable references for secrets.
- Review every server's capabilities and grant only the access needed for the project.
- Check whether the configuration is intended to be committed or kept local.

MCP availability and configuration options depend on the installed VS Code version and extensions. See the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) for current details.
