---
layout: post
title:  "Release schedule"
date:   2019-02-17 17:14:40
author: Alexandros Theodotou
---
## An introduction to the project
Zrythm started development in July 2018 and has only recently started to become slightly usable. Here is a list of features that are somewhat implemented (but not necessarily stable/perfected).

### Loading plugins
Most LV2 plugins out there at the moment will work fine, with the exception of some plugins written in toolkits incompatible with Gtk. Those plugins will show a generic UI instead. Plugins can be placed in channels and tracks and used like in other DAWs, with a few cases where they might crash. This will be fixed soon.
<img src="/img/loading_plugins.png" alt="Loading plugins"/>

### MIDI note recording/playback
MIDI recording has only recently been implemented and somewhat works but still needs fixes and improvement. Drawing notes and regions also works, and some copy/paste/delete functionality is there but not very stable at the moment.
<img src="/img/midi_playback.png" alt="MIDI playback"/>

### Audio tracks
This wasn't in the original scope, but it is quite easy to implement, so audio channels can be created just by draggin and dropping samples in the tracklist! OGG/FLAC/WAV and if FFMPEG is available, MP3 is also supported. Audio regions cannot be resized or edited at the moment, only repositioned.
<img src="/img/audio_track.png" alt="Audio tracks"/>

### Pans, faders, mute/solo
These should work mostly fine by now.
<img src="/img/pans_faders_mute.png" alt="Pans, faders, mute/solo"/>

### Project saving/loading
It was once implemented in XML, then broken, and now is being implemented in YAML! Saving is functional and loading is currently being fixed/re-implemented.
<img src="/img/saving.png" alt="Saving"/>

### Exporting
The selected loop or the whole song can be exported in various formats. Currently, OGG/FLAC/WAV and if ffmpeg is available MP3 are supported.
<img src="/img/export.png" alt="Exporting"/>

### Automating plugin parameters
This was somewhat functional but currently broken and being fixed. Automation curves are supported!
<img src="/img/automation.png" alt="Automation curves"/>

# What's left to do?
A lot of things, but most of the critical functionality and the backbone is there. A list of pending issues can be found in the <a href="https://git.zrythm.org/zrythm/zrythm/issues">issue tracker</a>. One important thing that is missing is the ability to easily connect plugin ports and automate them via built-in LFOs and various envelopes. Those will be worked on after the first release when Zrythm becomes a little more stable.

# So when can I try it?
Zrythm is readily available in Arch GNU/Linux via the zrythm-git package in AUR. RPM and .deb packages are also being built but not as easy to install at the moment. They will be available once Zrythm has its first release (which will be an alpha release mainly for testing, but hopefully also usable for making music).

Zrythm's first alpha release will be on April 15, 2019, as is customary in the GNU/Linux audio community. Zrythm has been in development for six months and there is still a lot of work, but it is slowly starting to become more and more usable, and more fun to work with. Testers are welcome. If you would like to financially support our work you may do so <a href="https://www.zrythm.org/donate/">here</a>
