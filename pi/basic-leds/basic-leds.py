#!/usr/bin/env python

import argparse
import logging
import RPi.GPIO as GPIO
import time

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

DEFAULT_INTERVAL = 1   # in seconds

logger = logging.getLogger(__name__)


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)

    alloff()


def teardown():
    alloff()
    GPIO.cleanup()


def alloff():
    GPIO.output(LED_R, OFF)
    GPIO.output(LED_G, OFF)
    GPIO.output(LED_B, OFF)


def counter(interval=DEFAULT_INTERVAL):

    for i in xrange(8):
        logging.info("  %d", i)

        GPIO.output(LED_R, ON if i & 0b100 else OFF)
        GPIO.output(LED_G, ON if i & 0b010 else OFF)
        GPIO.output(LED_B, ON if i & 0b001 else OFF)

        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')

    opts = parser.parse_args()

    logging.basicConfig(level=opts.debug)
    logger.debug('opts="%s"',  opts)

    setup()

    logging.info("Starting...")

    while True:

        try:
            counter()

        except KeyboardInterrupt:
            break

        except:
            logging.exception()

    logging.info("done.")

    teardown()


if __name__ == '__main__':
    main()
