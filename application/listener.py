import logging
import throttle
import button
import sound
import pushover
import config

log = logging.getLogger(__name__)

throttle = throttle.Throttler()

def checkBell():
    if (button.pressed()):
        notify()
        return True
    else:
        return False

def notify():
    log.info('Doorbell pressed')
    sound.play()

    if throttle.check():
        pushover.send(config.message_text)
    else:
        log.info('THROTTLING')