#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Marcel Eggert"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"

"""ssl-test.py: Description of what foobar does."""

import sslTester


def main():
    import argparse
    import sys

    mx = False

    parser = argparse.ArgumentParser()

    parser.add_argument('--domain',
                        dest='domain',
                        help='Domain welche abgefragt werden soll')

    parser.add_argument('--mx',
                        dest='mx',
                        action='store_true',
                        default=False,
                        help='get mx records and start the ssl tests for it')

    args = parser.parse_args()

    if args.mx:
        mx = True

    ssl = sslTester.sslTester()

    ssl.initial()

    ssl.start_check()

    rec = ssl.host_lookup(args.domain, mx)
    print(rec)


if __name__ == '__main__':
    main()
