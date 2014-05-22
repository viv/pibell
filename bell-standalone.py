#!/usr/bin/env python

from time import sleep
from time import time
import subprocess
import httplib, urllib
import config
import logger

LOW_PRIORITY = -1
MEDIUM_PRIORITY = 0
HIGH_PRIORITY = 1

rate = 1.0; # unit: messages
perSecond  = 15.0; # unit: seconds
allowance = rate; # unit: messages
last_check = int(time()); # floating-point, e.g. usec accuracy. Unit: seconds

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

def playSound():
    subprocess.Popen(["ogg123","-q","dingdong.ogg"])

def buttonPressed():
    log.info('Doorbell pressed')
    playSound()
    notifyPhones(config.message_text)
    sleep(3);

notifyPhones('Listener started', LOW_PRIORITY)
log.info('Doorbell listener Started')

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
            subprocess.Popen(["ogg123","-q","dingdong.ogg"])
        else:
            buttonPressed()
            allowance -= 1.0;
