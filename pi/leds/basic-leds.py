#!/usr/bin/env python

import argparse
import logging
import importlib

import control

logger = logging.getLogger(__name__)

DEFAULT_INTERVAL = 0.5   # seconds


def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')
    parser.add_argument('-p', '--plugin', type=str, default='counter', help='Which plugin to run (default: %(default)s)')
    parser.add_argument('-i', '--interval', type=str, default=DEFAULT_INTERVAL, help='seconds between steps (default: %(default)s)')

    opts = parser.parse_args()

    logging.basicConfig(level=opts.debug)
    logger.debug('opts="%s"',  opts)

    plugin = importlib.import_module('plugins.{}'.format(opts.plugin))

    control.setup()
    plugin.setup()

    logging.info("Starting...")

    while True:

        try:
            plugin.step(opts.interval)

        except KeyboardInterrupt:
            break

        except Exception, e:
            logging.exception(e)
            break

    logging.info("done.")

    plugin.teardown()
    control.teardown()


if __name__ == '__main__':
    main()
