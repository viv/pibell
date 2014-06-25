import sound
import logging
import pushover
import thingspeak
import config
import throttle

log = logging.getLogger(__name__)

throttle = throttle.Throttler()

def pressed():
    if throttle.check():
        log.info('Doorbell pressed')
        sound.play()
        pushover.send(config.message_text)
        thingspeak.update()
    else:
        log.info('THROTTLING')