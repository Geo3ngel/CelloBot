Built into [[Cello Bot Core]]
Dynamically extends via plugin blueprints
# **Core Features:**
- Plugin manager UI
- Configuration UI
- Visual representation of recordings (waveform preview)
	- Should this be built into the primary application? Or plugin dependent?
	- Probably considered a primary thing for now... idk.
- OBS integration panel
## How Plugins Modify the Flask UI

**How to extend Flask dynamically?**
- Use **Flask Blueprints** for modular UI extensions.
- Each plugin **registers a UI component** via Core.
- Core automatically loads active plugins’ UI routes.
# Potential Issues
Flask is blocking by default. `quart` might be a better alternative for an async web server.
WebSocket support needed for real-time updates!
- This is totally fine to support by me!