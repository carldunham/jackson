#!/usr/bin/python

##----------------------------------------------------------------------
## Copyright (c) 2013 Jackson Dunham, All Rights Reserved
##----------------------------------------------------------------------
##
## testone.py
##
## Created: 2013-10-15 by jackson
##
##----------------------------------------------------------------------

"""
this is a test to see if i can use this program :D
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

    for i in range(5):
        print "i know what this %d command does now i relays with out knowing it!" % (i)

        if i==3:
            print "I'm a boss at this now!"
    if True:
        print "hello i learned this form when direwolf20 played with computer craft in this seson 3 lp!"
    # ends here

    
if __name__ == "__main__":
    main()
