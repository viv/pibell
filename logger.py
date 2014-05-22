import logging
import logging.handlers

tenMegabytesInBytes = 10485760

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler = logging.handlers.RotatingFileHandler(
              'application.log', maxBytes=tenMegabytesInBytes, backupCount=5)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

def get(name):
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger