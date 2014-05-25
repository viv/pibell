import logging
import logging.handlers

tenMegabytesInBytes = 10485760

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler = logging.handlers.RotatingFileHandler(
              'application.log', maxBytes=tenMegabytesInBytes, backupCount=5)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

rootLogger = logging.getLogger()
rootLogger.addHandler(handler)
rootLogger.setLevel(logging.DEBUG)