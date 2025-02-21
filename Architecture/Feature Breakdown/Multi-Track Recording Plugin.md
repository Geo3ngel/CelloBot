---
Created: 2025/02/19 23:40
Type: "[[Plugin]]"
"Tags:":
---
**v0 Goal:** Record each user as a separate audio file, tagging their User ID.

## Implementation
### Capturing Discord Audio

### Store Metadata
Store user IDs & timestamps in a JSON database.
### Handle Disconnects Gracefully
Detect leave events & stop track recording for that user.
- how to adjust/add to their track if they come back in though? Can this be done in a way that is efficient storage space wise?
# Potential Issues
- Real-time audio processing is CPU-intensive.
- A **separate process/thread** should handle encoding to avoid blocking.