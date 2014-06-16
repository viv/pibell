#!/usr/bin/env python

import logging
from application import listener, logsetup, pushover

log = logging.getLogger(__name__)

log.info('Doorbell listener Started')
pushover.send('Listener started', pushover.LOW_PRIORITY)

while True:
  listener.checkBell()