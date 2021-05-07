#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Marcel Eggert"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"

"""ssl-test.py: """

import sslTester


def main():
    import argparse
    import sys

    mx = False

    parser = argparse.ArgumentParser()

    parser.add_argument('--domain',
                        dest='domain',
                        help='Domain welche abgefragt werden soll',
                        required=True)

    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        help='Port für die Connection',
                        required=True)
    
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

    records = ssl.host_lookup(args.domain, mx)

    if mx:
        for rec in records:
            ssl.start_check(rec, args.port)
    else:
        ssl.start_check(records, args.port)


if __name__ == '__main__':
    main()
