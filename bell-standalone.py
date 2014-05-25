#!/usr/bin/env python

from time import sleep
import logging
from application import logsetup, button, pushover

log = logging.getLogger(__name__)

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

while True:
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        break
    else:
        button.pressed()
        sleep(3)