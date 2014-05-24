#!/usr/bin/env python

from time import sleep
import config
import logsetup
import logging
import pushover
import sound
from application import throttle

log = logging.getLogger(__name__)

throttle = throttle.Throttler()

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

def buttonPressed():
    log.info('Doorbell pressed')
    sound.play()

    if throttle.check():
        pushover.send(config.message_text)
    else:
        log.info('THROTTLING')

while True:
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        break
    else:
        buttonPressed()
        sleep(3)