
import logging
import time

from .. import control

INTERVAL = 0.5   # seconds


def setup():
    pass


def teardown():
    pass


def step():

    for i in xrange(8):
        logging.info("  %d", i)

        control.red(i & 0b100)
        control.green(i & 0b010)
        control.blue(i & 0b001)

        time.sleep(INTERVAL)
