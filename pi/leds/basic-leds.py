#!/usr/bin/env python

import argparse
import logging

import control

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Control red, green and blue LEDs')
    parser.add_argument('-d', '--debug', type=str, default='INFO', help='set debug level to DEBUG (default: %(default)s)')
    parser.add_argument('-p', '--plugin', type=str, default='counter', help='Which plugin to run (default: %(default)s)')

    opts = parser.parse_args()

    logging.basicConfig(level=opts.debug)
    logger.debug('opts="%s"',  opts)

    plugin = __import__('plugins', fromlist=[opts.plugin])

    control.setup()
    plugin.setup()

    logging.info("Starting...")

    while True:

        try:
            plugin.step()

        except KeyboardInterrupt:
            break

        except:
            logging.exception()

    logging.info("done.")

    plugin.teardown()
    control.teardown()


if __name__ == '__main__':
    main()
