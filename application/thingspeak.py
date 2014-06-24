import logging
import httplib, urllib
import config

log = logging.getLogger(__name__)

def update():
    log.debug('Updating thingspeak')
    conn = httplib.HTTPSConnection("api.thingspeak.com:443")
    conn.request("POST", "/update",
    urllib.urlencode({
        "api_key": config.thingspeak_write_api_key,
        "field1": 1,
    }), { "Content-type": "application/x-www-form-urlencoded" })

    response = conn.getresponse()
    log.debug('Got response: '
                + str(response.status)
                + ' ' + response.reason
                + ': ' + response.read())
    conn.close()
