#!/usr/bin/python

##----------------------------------------------------------------------
## Copyright (c) 2013 Jackson Dunham, All Rights Reserved
##----------------------------------------------------------------------
##
## template.py
##
## Created: 2013-MMM-dd by jackson
##
##----------------------------------------------------------------------

"""
Basic Description
"""

import sys
import os
from optparse import OptionParser

DEBUG = 0


def main():
    """
    This is the main function for the module. 
    """

    parser = OptionParser(version="0.1", usage="%prog [options]")
    parser.add_option("-d", "--debug", type="int", default=0, help="set debug level to DEBUG (default: %default)")
    parser.add_option("-q", "--quiet", action="store_true", dest="quiet")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")

    (opts, args) = parser.parse_args()

    global DEBUG
    DEBUG = opts.debug

    if DEBUG >= 3:
        print >> sys.stderr, 'opts="%s"' % opts

    # code starts here

    # ends here

    
if __name__ == "__main__":
    main()
