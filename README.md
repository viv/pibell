Doorbell Listener
====================
Waits for a signal, plays a sound and sends a pushover message to mobile devices.

For Ogg playback:
`sudo apt-get install vorbis-tools`

Doorbell audio taken from http://commons.wikimedia.org/wiki/File:Doorbell-cheap-dingdong.ogg

If you get this error: `Error: ALSA lib pcm.c:2217:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.front`

Edit `/usr/share/alsa/alsa.conf` change the line `pcm.front cards.pcm.front` to `pcm.front cards.pcm.default`
