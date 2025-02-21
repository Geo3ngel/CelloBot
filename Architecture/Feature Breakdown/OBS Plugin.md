---
Created: 2025/02/19 23:40
Type: "[[Plugin]]"
"Tags:":
---
**Goal:** Display recording status in OBS & Web UI.
## Implementation
OBS connects to Core via gRPC
Plugin listens for recording state changes.
OBS Plugin receives updates & shows UI overlay
- might not be necessary, since we're using the CORE web interface to tell if we're still recording and what not!
### Additional features I wanna try to add later:
Synchronization of the audio being recorded via the bot with the OBS recording via time stamps if possible to assist with alignment?
- even if this is just marking time stamps

Maybe setting up time stamps for when people join/leave, if we're doing separate recording audio files to save space or something? 