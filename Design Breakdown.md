---
Created: "2025/02/19 21:39"
Status: fleeting
"Tags:":
---
# Features
## Multi-track recording
Record individual users in the call as separate audio tracks!
- have some way of marking the time stamp at which they join if adding them in real time!
- gracefully handle people leaving/rejoining
	- Tag audio tracks for them by user ID!
**Requires** the [[Discord Audio Interface Sink]] to be running first in Core
## OBS Plugin
Have an OBS plugin for communicating between OBS & the core application to show when we're recording!
- displays something in the Web Interface!
The idea being to enable us to map the audio to the recording properly, and even mark important moments!

## Transcription Plugin
Maybe even transcribe what each person is saying?
- Either in post, or in real time!
	- real time would allow for Alexa esc features, like a keyword trigger followed by some command from a specific use to do something/play a sfx for example!
- Would be cool if I could eventually use this feature to auto break things up into segments!
**Requires**:
- Multi-track recording

## Web Interface Control/Debug Panel [Application]
A Web interface for controlling everything! (Using Flask)
- would this be built into core? Probably.
### Toggling/adding plugins
### Setting up configurations
### Display Audio tracks being recorded 
[This would be a Plugin thing]
- Feature added via Multi-track recording plugin maybe?
	- How could I go about adding web interface stuffs via plugins?
	- Or should I have it built into the main app, and toggled on when the plugin is enabled?
		- This would imply the Multi-track-recording plugin should be a part of the core application.
Show the wave form, and associated Discord user ID! [Maybe even their profile pic ideally :)]
### Sound board [Plugin]
Playing audio through CelloBot!
**Requires** the [[Discord Audio Interface Sink]] to be running first in Core
### Music Queue [Plugin]
A visual representation of the music queue!
- easy ability to add songs from various places!
**Requires** the [[Discord Audio Interface Sink]] to be running first in Core

The concept of using Plugins/Applications in addition to the base Core is to allow the application future flexibility for adding more features as needed!
- In addition to providing services via plugins for the core application, I also want to enable these to affect the Flask UI. How might I go about doing this?

I'm building this out using Python 3.11.9
Using gRpc for server/client communication
- Could I use this to communicate between multiple apps/clients run locally? 

---
# References