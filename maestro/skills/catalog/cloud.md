# Cloud and platform (plugins OFF by default)
name | source | use when | do NOT use when | conflict/preference
Source codes and global choice rules: see ../CATALOG.md

airunway-aks-setup | AZ | Set up AI Runway on AKS — from bare cluster… | non-Azure projects | -
appinsights-instrumentation | AZ | Guidance for instrumenting webapps with Azur… | non-Azure projects | -
azure-ai | AZ | Use for Azure AI: Search, Speech, OpenAI, Do… | non-Azure projects | -
azure-aigateway | AZ | Configure Azure API Management as an AI Gate… | non-Azure projects | -
azure-app-onboard | AZ | End-to-end orchestrator: from a business ide… | non-Azure projects | -
azure-app-onboard-prereq | AZ | Assess whether source code is ready to deplo… | non-Azure projects | -
azure-cloud-migrate | AZ | Assess and migrate cross-cloud workloads to… | non-Azure projects | -
azure-compliance | AZ | Run Azure compliance and security audits wit… | non-Azure projects | -
azure-compute | AZ | Azure VM/VMSS router | non-Azure projects | -
azure-deploy | AZ | Execute Azure deployments for ALREADY-PREPAR… | non-Azure projects | -
azure-diagnostics | AZ | Debug Azure production issues on Azure using… | non-Azure projects | -
azure-enterprise-infra-planner | AZ | Architect and provision enterprise Azure inf… | non-Azure projects | -
azure-kubernetes | AZ | Plan, create, and configure production-ready… | non-Azure projects | -
azure-kusto | AZ | Query and analyze data in Azure Data Explore… | non-Azure projects | -
azure-messaging | AZ | Troubleshoot and resolve issues with Azure M… | non-Azure projects | -
azure-prepare | AZ | Prepare azd-based Azure projects for deploym… | non-Azure projects | -
azure-quotas | AZ | Check/manage Azure quotas and usage across p… | non-Azure projects | -
azure-reliability | AZ | Assess and improve the reliability posture o… | non-Azure projects | -
azure-resource-lookup | AZ | List, find, and show Azure resources across… | non-Azure projects | -
azure-resource-visualizer | AZ | Analyze Azure resource groups and generate d… | non-Azure projects | -
azure-storage | AZ | Azure Storage Services including Blob Storag… | non-Azure projects | -
azure-upgrade | AZ | Assess and upgrade Azure workloads between p… | non-Azure projects | -
azure-validate | AZ | Pre-deployment validation for Azure readines… | non-Azure projects | -
discover-azure-skills | AZ | Searches the Azure skills catalog and recomm… | non-Azure projects | -
entra-agent-id | AZ | Provision Microsoft Entra Agent Identity Blu… | non-Azure projects | -
entra-app-registration | AZ | Guides Microsoft Entra ID app registration… | non-Azure projects | -
microsoft-foundry | AZ | Build, deploy, evaluate, optimize, fine-tune… | non-Azure projects | -
python-appservice-deploy | AZ | Deploy Python (Flask/Django/FastAPI) code to… | non-Azure projects | -
csharp-expert | DN/dotnet | Route C# and .NET requests to the exact inst… | non-.NET projects | -
csharp-refactoring | DN/dotnet | Safely refactors C#/.NET code without changi… | non-.NET projects | -
msbuild | DN/dotnet | Use only for MSBuild failure investigation… | non-.NET projects | -
setup-local-sdk | DN/dotnet | Install a .NET SDK locally for safe preview… | non-.NET projects | -
convert-blazor-server-to-webapp | DN/dotnet-aspnetcore | Guides conversion of a pre-.NET 8 Blazor Ser… | non-.NET projects | -
dotnet-webapi | DN/dotnet-aspnetcore | Guides creation and modification of ASP.NET… | non-.NET projects | -
create-datadriven-aspnetcore | DN/dotnet-data | Generate or scaffold ASP.NET Core code — Raz… | non-.NET projects | -
optimizing-ef-core-queries | DN/dotnet-data | Review and optimize application data access… | non-.NET projects | -
analyzing-dotnet-performance | DN/dotnet-diag | Scans .NET code for ~50 performance anti-pat… | non-.NET projects | -
android-tombstone-symbolication | DN/dotnet-diag | Symbolicate the .NET runtime frames in an An… | non-.NET projects | -
apple-crash-symbolication | DN/dotnet-diag | Symbolicate .NET runtime frames in Apple pla… | non-.NET projects | -
clr-activation-debugging | DN/dotnet-diag | Diagnoses .NET Framework CLR activation issu… | non-.NET projects | -
dotnet-trace-collect | DN/dotnet-diag | Guide developers through capturing diagnosti… | non-.NET projects | -
dump-collect | DN/dotnet-diag | Configure and collect crash dumps for modern… | non-.NET projects | -
microbenchmarking | DN/dotnet-diag | Activate this skill when BenchmarkDotNet (BD… | non-.NET projects | -
assertion-quality | DN/dotnet-test | Analyze assertion quality, depth, variety, a… | non-.NET projects | -
code-testing | DN/dotnet-test | ALWAYS USE for test work that requires chang… | non-.NET projects | -
code-testing-agent | DN/dotnet-test | Legacy compatibility alias for the code-test… | non-.NET projects | -
code-testing-extensions | DN/dotnet-test | Provides file paths to language-specific ext… | non-.NET projects | -
coverage-analysis | DN/dotnet-test | Activation requires either supplied .NET cov… | non-.NET projects | -
crap-score | DN/dotnet-test | Calculates CRAP (Change Risk Anti-Patterns)… | non-.NET projects | -
detect-static-dependencies | DN/dotnet-test | ACTIVATION PREREQUISITE: the request or disc… | non-.NET projects | -
filter-syntax | DN/dotnet-test | Reference-only filter syntax for VSTest and… | non-.NET projects | -
find-untested-sources | DN/dotnet-test | MANDATORY for static source-to-test pairing:… | non-.NET projects | -
generate-testability-wrappers | DN/dotnet-test | DO NOT USE when the target already consumes… | non-.NET projects | -
grade-tests | DN/dotnet-test | Grade curated individual tests for readiness… | non-.NET projects | -
migrate-static-to-wrapper | DN/dotnet-test | ALWAYS USE when asked to migrate, replace, o… | non-.NET projects | -
mtp-hot-reload | DN/dotnet-test | Set up or recover MTP hot reload for a long-… | non-.NET projects | -
platform-detection | DN/dotnet-test | Identify a .NET project's test platform, fra… | non-.NET projects | -
run-tests | DN/dotnet-test | ALWAYS USE before running .NET tests or answ… | non-.NET projects | -
scaffold-dotnet-test-project | DN/dotnet-test | MUST USE when an existing .NET test project… | non-.NET projects | -
test-analysis-extensions | DN/dotnet-test | Provides file paths to language-specific ref… | non-.NET projects | -
test-anti-patterns | DN/dotnet-test | Audit a test file or suite; produce a severi… | non-.NET projects | -
test-gap-analysis | DN/dotnet-test | Find caller-visible production changes exist… | non-.NET projects | -
test-smell-detection | DN/dotnet-test | Audits existing tests in any language using… | non-.NET projects | -
test-tagging | DN/dotnet-test | Classifies existing tests by standard traits… | non-.NET projects | -
test-value-evidence | DN/dotnet-test | Assess tests for an identified code or test… | non-.NET projects | -
testability-obstacle | DN/dotnet-test | MUST USE for C#/.NET deterministic tests tha… | non-.NET projects | -
writing-mstest-tests | DN/dotnet-test | ALWAYS USE when asked to fix, rewrite, updat… | non-.NET projects | -
dotnet-aot-compat | DN/dotnet-upgrade | Make .NET projects compatible with Native AO… | non-.NET projects | -
migrate-dotnet10-to-dotnet11 | DN/dotnet-upgrade | Migrate a .NET 10 project or solution to .NE… | non-.NET projects | -
migrate-dotnet8-to-dotnet9 | DN/dotnet-upgrade | Migrate a .NET 8 project to .NET 9 and resol… | non-.NET projects | -
migrate-dotnet9-to-dotnet10 | DN/dotnet-upgrade | Migrate a .NET 9 project or solution to .NET… | non-.NET projects | -
migrate-nullable-references | DN/dotnet-upgrade | Enable nullable reference types in a C# proj… | non-.NET projects | -
thread-abort-migration | DN/dotnet-upgrade | Guides migration of .NET Framework Thread.Ab… | non-.NET projects | -
finding-google-skills | GC | Google platform decision and setup guidance… | non-GCP; MCP needs API key | -
gcloud | GC | Provides safety-critical validation, guardra… | non-GCP; MCP needs API key | -
google-cloud-recipe-auth | GC | Provides expert guidance on Identity and Acc… | non-GCP; MCP needs API key | -
google-cloud-recipe-onboarding | GC | Guides a developer's first steps on Google C… | non-GCP; MCP needs API key | -
retrieving-developer-knowledge | GC | Searches, retrieves, and synthesizes officia… | non-GCP; MCP needs API key | -
n8n-agents | N8 | Design n8n AI agents the right way | non-n8n; hooks cannot be split | -
n8n-binary-and-data | N8 | Handle files and binary data in n8n correctl… | non-n8n; hooks cannot be split | -
n8n-code-javascript | N8 | Write JavaScript code in n8n Code nodes | non-n8n; hooks cannot be split | -
n8n-code-python | N8 | Write Python in n8n Code nodes (native Pytho… | non-n8n; hooks cannot be split | -
n8n-code-tool | N8 | Write JavaScript or Python for the n8n Custo… | non-n8n; hooks cannot be split | -
n8n-error-handling | N8 | Wire n8n error handling so failures are loud… | non-n8n; hooks cannot be split | -
n8n-expression-syntax | N8 | Validate n8n expression syntax and fix commo… | non-n8n; hooks cannot be split | -
n8n-mcp-tools-expert | N8 | Expert guide for using n8n-mcp MCP tools eff… | non-n8n; hooks cannot be split | -
n8n-multi-instance | N8 | Use when an n8n-mcp account targets more tha… | non-n8n; hooks cannot be split | -
n8n-node-configuration | N8 | Operation-aware node configuration guidance | non-n8n; hooks cannot be split | -
n8n-self-hosting | N8 | Deploy a production self-hosted n8n end-to-e… | non-n8n; hooks cannot be split | -
n8n-subworkflows | N8 | Build reusable, composable n8n sub-workflows | non-n8n; hooks cannot be split | -
n8n-validation-expert | N8 | Interpret validation errors and guide fixing… | non-n8n; hooks cannot be split | -
n8n-workflow-patterns | N8 | Proven workflow architectural patterns from… | non-n8n; hooks cannot be split | -
using-n8n-mcp-skills | N8 | Use when building, editing, validating, test… | non-n8n; hooks cannot be split | -
