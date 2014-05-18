#!/usr/bin/env python

from time import sleep
import subprocess
import httplib, urllib
import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.bell_pin, GPIO.IN)

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
print 'Doorbell listener Started\r'

while True:
    if (GPIO.input(23) == False):
        subprocess.Popen(["ogg123","-q","dingdong.ogg"])
        notifyPhones(config.message_text)
        sleep(3);