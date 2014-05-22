#!/usr/bin/env python

from time import sleep
import subprocess
import httplib, urllib
import RPi.GPIO as GPIO
import config
import logger

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.bell_pin, GPIO.IN)

LOW_PRIORITY = -1
MEDIUM_PRIORITY = 0
HIGH_PRIORITY = 1

log = logger.get(__name__)

def notifyPhones(message, priority=MEDIUM_PRIORITY):
    log.debug('Sending pushover message "'
                 + message
                 + '" with priority '
                 + str(priority))
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
        "token": config.application_token,
        "user": config.user_token,
        "title": config.message_title,
        "message": message,
        "url": config.message_url,
        "priority": priority,
    }), { "Content-type": "application/x-www-form-urlencoded" })

    response = conn.getresponse()
    log.debug('Got response: '
                + str(response.status)
                + ' ' + response.reason
                + ': ' + response.read())
    conn.close()

notifyPhones('Listener started', LOW_PRIORITY)
log.info('Doorbell listener Started')

while True:
    if (GPIO.input(23) == False):
        subprocess.Popen(["ogg123","-q","dingdong.ogg"])
        notifyPhones(config.message_text)
        log.info('Doorbell pressed')
        sleep(3);