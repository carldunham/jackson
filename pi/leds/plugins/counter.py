
import logging
import time

import leds

INTERVAL = 0.5   # seconds


def setup():
    pass


def teardown():
    pass


def step():

    for i in xrange(8):
        logging.info("  %d", i)

        leds.red(i & 0b100)
        leds.green(i & 0b010)
        leds.blue(i & 0b001)

        time.sleep(INTERVAL)
