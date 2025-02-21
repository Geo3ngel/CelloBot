# Responsibilities
- Independent modules that extend functionality
- Communicate with Core via gRPC
- Provide additional gRPC services if needed
# Architecture
Plugins interact with **Core via gRPC**.

They should be **isolated processes** (subprocess or separate microservices).

Each plugin should register itself with **Core** when enabled.

## Implementation:
1. Core has a `plugins/` directory where each plugin is a submodule.
2. Each plugin defines its gRPC service (if needed).
3. Plugins should have a **Flask Blueprint** if they extend the Web UI.

## Plugin Lifecycle:
- Plugin Manager loads/unloads them dynamically.
- Uses a `config.json` for enabling/disabling plugins.
- Implements event listeners for Discord-related events.

## Communication Flow:
- Plugins register with Core on startup.
- Core exposes a `PluginManager` API to list and control them.
# Potential Issues
- UI plugins need to register their Flask blueprints dynamically.
- Some gRPC messages might need **broadcasting** to multiple clients.