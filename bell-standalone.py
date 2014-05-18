#!/usr/bin/env python

from time import sleep
import subprocess
import httplib, urllib
import config
import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('application.log')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

logger.setLevel(logging.INFO)
logger.addHandler(handler)

LOW_PRIORITY = -1
MEDIUM_PRIORITY = 0
HIGH_PRIORITY = 1

def notifyPhones(message, priority=MEDIUM_PRIORITY):
    logger.debug('Sending pushover message "'
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
    logger.debug('Got response: '
                + str(response.status)
                + ' ' + response.reason
                + ': ' + response.read())
    conn.close()

notifyPhones('Listener started', LOW_PRIORITY)
logger.info('Doorbell listener Started')

while True:
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        break
    else:
        subprocess.Popen(["ogg123","-q","dingdong.ogg"])
        notifyPhones(config.message_text)
        logger.info('Doorbell pressed')
        sleep(3);