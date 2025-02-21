---
Created: "2025/02/19 23:42"
Type: "[[Plugin]]"
"Tags:":
---
**Goal:** Play audio through the bot.

**Implementation:**
1. Core exposes a `/play` gRPC method. [debatable]
	1. Maybe we make this some "play audio" method that can take in whatever byte string audio wise
2. Flask UI provides a **button-based interface** to trigger sounds.
3. Bot streams **audio via Lavalink or FFmpeg**.

---
# Potential Issues
Handling overlapping sounds requires a [mixer]
- Should work this into the implementation
# Requires
[[Discord Audio Interface Sink]]