#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ssl-test.py: Description of what foobar does."""

import sslTester
__author__ = "Marcel Eggert"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser()

    parser.add_argument('--mx',
                        dest='mx',
                        action='store_true',
                        default=False,
                        help='get mx records and start the ssl tests for it')

    args = parser.parse_args()

    # if args.mx:
    #     self.mx = True

    args_dict = vars(args)

    ssl = sslTester.sslTester()
    
    ssl.initial()

if __name__ == '__main__':
    main()
