---
Created: 2025/02/19 23:49
Type: "[[Plugin]]"
"Tags:":
---
**Goal:** Manage & visualize a playlist.

**Implementation:**
1. UI fetches queue state via **Flask API**.
2. Bot plays songs via Lavalink.
3. Users can add/remove songs via UI or Discord chat.
	- Debating if I want to add flexibility for both here.
	- How would I make the discord commands also expandable based on the plugins added?

---
# Potential Issues
Handling multiple sources (Spotify, YouTube) requires further API integrations

---
# Requires
[[Discord Audio Interface Sink]]