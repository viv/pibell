#!/usr/bin/env python

from time import sleep
import subprocess
import httplib, urllib
import config
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('application.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger.addHandler(handler)

LOW_PRIORITY = -1
MEDIUM_PRIORITY = 0
HIGH_PRIORITY = 1

def notifyPhones(message, priority=MEDIUM_PRIORITY):
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

    conn.getresponse()

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