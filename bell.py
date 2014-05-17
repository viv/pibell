#!/usr/bin/env python

from time import sleep
import subprocess
import httplib, urllib
import config

def notifyPhones(message):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
        "token": config.application_token,
        "user": config.user_token,
        "title": config.message_title,
        "message": message,
        "url": config.message_url,
    }), { "Content-type": "application/x-www-form-urlencoded" })

    conn.getresponse()

notifyPhones('Listener started')
print 'Doorbell listener Started\r'

while True:
    key = raw_input("Hit a key, press Q to quit: ")
    if key.lower() == "q":
        break
    else:
        print 'Button Pushed!\r'
        subprocess.Popen(["ogg123","-q","dingdong.ogg"])
        notifyPhones(config.message_text)
        sleep(3);