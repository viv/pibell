import config
import logging
from application import logsetup

log = logging.getLogger(__name__)

try:
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(config.bell_pin, GPIO.IN)
	log.debug('Loaded GPIO module')

	def pressed():
		return (GPIO.input(23) == False)

except ImportError:
	print 'Failed to load GPIO module'
	log.debug('Failed to load GPIO module')
