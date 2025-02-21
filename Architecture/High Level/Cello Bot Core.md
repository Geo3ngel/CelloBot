# Code Base Responsibilities
- Manages plugins and services
- Handles gRPC server for communication
- Interfaces with Discord (via Lavalink, PyNaCl, or other VoIP solutions)
- Provides the Flask Web UI
## Description
- Acts as the main orchestrator of the bot.
- Hosts the gRPC server.
- Manages plugin registration and activation.
- Serves the Flask [[Web Interface]].
	- Dynamically extends via plugin blueprints
	- Displays real-time recording/transcription/OBS status using blueprints!
- Handles communication with Discord.
## Implementation:
- Use `discord.py` or `nextcord` for bot interaction.
- Use `gRPC` for inter-process communication.
- Use `Flask` for the web interface.
- Use `SQLAlchemy` or a lightweight database (SQLite/PostgreSQL) for storing user data.
# Potential Issues
- Flask is synchronous by default—consider running it in an async mode (`quart` could be an alternative).
- Recording Discord audio is **not native** to `discord.py`—you will need to use **ffmpeg & PyNaCl** or an external bot (e.g., Lavalink).
- Managing real-time audio transcription requires **low-latency processing** (potentially an issue with Python’s GIL).