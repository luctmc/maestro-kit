# Maestro plugin profiles (Claude Code)

All plugins below are installed (user scope) but DISABLED globally. Enable per project by adding
`enabledPlugins` to `<project>/.claude/settings.local.json` (personal) or `settings.json` (shared). Verified: project scope overrides user scope.
Always-on token cost is added per session only while enabled.

Globally ON (total ~5,267 tok): superpowers 848, ponytail 641, caveman 1,991, context7 0, skill-creator 114, mattpocock-skills 1,651, code-review 22, typescript-lsp 0, csharp-lsp 0, pyright-lsp 0 (+ RTK.md line).
RULE: azure, google-cloud-developer, dotnet*, n8n stay OFF globally. Maestro may enable them per project (or before recruiting a worker) when a mission needs them, and tells the user in one line.

| Profile | Plugins to enable (@marketplace) | Always-on tokens |
|---|---|---|
| web-ts | (already global: typescript-lsp, mattpocock-skills) | - |
| dotnet (CIINTEC backend) | (csharp-lsp already global) dotnet, dotnet-test, dotnet-aspnetcore, dotnet-diag, dotnet-data, dotnet-upgrade @dotnet-agent-skills | ~11,100 (dotnet-test alone ~5,557) |
| python | (already global: pyright-lsp) | - |
| azure | azure@azure-skills | ~6,268 |
| gcp | google-cloud-developer@google-plugins | ~838 |
| n8n | n8n-mcp-skills@n8n-mcp-skills | ~3,977 |

## Notes before enabling
- LSP plugins need their language-server binary (typescript-language-server, csharp-ls, pyright). Install on first activation, not before.
- azure: bundled MCP `azure` (npx -y @azure/mcp@latest) and hooks SessionStart/PostToolUse (track-telemetry.sh). Telemetry is off via env AZURE_MCP_COLLECT_TELEMETRY=false (script exits 0). MCP must be turned off via /mcp after enabling; verify at activation.
- google-cloud-developer: MCP developer-knowledge needs DEVELOPERKNOWLEDGE_API_KEY; do not set unless asked.
- n8n: hooks SessionStart (injects meta-skill, local, no network), PreToolUse on n8n MCP tools, PostToolUse. No per-hook switch exists; PENDING decision at activation (patch plugin cache copy or accept). Remote MCP api.n8n-mcp.com is not bundled by the plugin (0 servers), so nothing connects by default.
- Codex: no Step 2 plugins installed (per user decision: only on demand).
