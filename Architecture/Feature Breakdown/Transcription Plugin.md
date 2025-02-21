---
Created: 2025/02/19 23:40
Type: "[[Service]]"
"Tags:":
---
**Goal:** Convert recorded voice into text for further processing elsewhere
## Use cases:
### Verbal Bot Commands
Requires an additional [Text Processing Engine]!
- Depending on how this goes, this might better be described as a [Service] than a [Plugin
### Audio Seek
Easy seeking to audio/video markers via key phrases/words (more an editor thing)
- This would likely be another plugin that uses this transcription. Might be best to build out for Davinci Resolve or something!

> [!info] Needs Rework
## Implementation: 
1. Use **Whisper API / Deepgram / Vosk** for speech-to-text.
2. Provide **real-time transcription** via **WebSocket**.
3. Allow **keyword-based commands** (like Alexa).

---
# Potential Issues
- **High CPU usage** (offload to a separate process or use GPU).
- **Real-time vs. post-processing**:
    - Post-processing is more accurate.
    - Real-time allows interactive bot commands.

---
# References