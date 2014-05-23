import logging
import httplib, urllib
import config

LOW_PRIORITY = -1
MEDIUM_PRIORITY = 0
HIGH_PRIORITY = 1

log = logging.getLogger(__name__)

def send(message, priority=MEDIUM_PRIORITY):
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
