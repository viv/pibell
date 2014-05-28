#!/usr/bin/env python

import logging
import RPi.GPIO as GPIO
from application import logsetup, button, pushover

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.bell_pin, GPIO.IN)

log = logging.getLogger(__name__)

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

while True:
    if (GPIO.input(23) == False):
        button.pressed()