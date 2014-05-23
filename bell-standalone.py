#!/usr/bin/env python

from time import sleep
from time import time
import config
import logsetup
import logging
import pushover
import sound

rate = 1.0; # unit: messages
perSecond  = 15.0; # unit: seconds
allowance = rate; # unit: messages
last_check = int(time()); # floating-point, e.g. usec accuracy. Unit: seconds

log = logging.getLogger(__name__)

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

def buttonPressed():
    log.info('Doorbell pressed')
    sound.play()
    pushover.send(config.message_text)
    sleep(3);

while True:
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        break
    else:
        current = int(time());
        time_passed = current - last_check;
        last_check = current;
        allowance += time_passed * (rate / perSecond);

        if (allowance > rate):
            allowance = rate; # throttle

        if (allowance < 1.0):
            log.info('THROTTLING')
            sound.play()
        else:
            buttonPressed()
            allowance -= 1.0;
