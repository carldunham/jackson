
import logging
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):

    for i in xrange(8):
        logging.info("  %d", i)

        control.red(i & 0b100)
        control.green(i & 0b010)
        control.blue(i & 0b001)

        time.sleep(interval)
