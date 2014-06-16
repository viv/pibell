#!/usr/bin/env python

import logging
import sys
from application import listener, logsetup, pushover, button

def pressed():
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        sys.exit(0)
    else:
        return True

button.pressed = pressed

log = logging.getLogger(__name__)

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

while True:
  listener.checkBell()