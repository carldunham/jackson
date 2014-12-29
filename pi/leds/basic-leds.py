#!/usr/bin/env python

import time
import argparse
import logging
import importlib

import control

logger = logging.getLogger(__name__)

DEFAULT_INTERVAL = 0.5   # seconds

MIN_INTERVAL = 0.01
MAX_INTERVAL = 8

_interval = DEFAULT_INTERVAL
_pause = False


def _handle_button(button):
    logger.info("Button Press: %d", button)

    if button == control.RESET_BUTTON:
        global _pause
        _pause = not _pause

    elif button == control.LEFT_BUTTON:
        global _interval
        _interval = max(MIN_INTERVAL, _interval / 2.0)

    elif button == control.RIGHT_BUTTON:
        global _interval
        _interval = min(MAX_INTERVAL, _interval * 2.0)


def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')
    parser.add_argument('-p', '--plugin', type=str, default='counter', help='Which plugin to run (default: %(default)s)')
    parser.add_argument('-i', '--interval', type=str, default=DEFAULT_INTERVAL, help='seconds between steps (default: %(default)s)')

    opts = parser.parse_args()

    logging.basicConfig(level=opts.debug)
    logger.debug('opts="%s"',  opts)

    plugin = importlib.import_module('plugins.{}'.format(opts.plugin))

    global _interval
    _interval = float(opts.interval)

    control.setup(button_function=_handle_button)
    plugin.setup()

    logger.info("Starting...")

    while True:

        try:
            if _pause:
                time.sleep(1)
            else:
                plugin.step(_interval)

        except KeyboardInterrupt:
            break

        except Exception, e:
            logger.exception(e)
            break

    logger.info("done.")

    plugin.teardown()
    control.teardown()


if __name__ == '__main__':
    main()
