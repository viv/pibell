import sound
import logging
import pushover
import config
import throttle

log = logging.getLogger(__name__)

throttle = throttle.Throttler()

def pressed():
    log.info('Doorbell pressed')
    sound.play()

    if throttle.check():
        pushover.send(config.message_text)
    else:
        log.info('THROTTLING')