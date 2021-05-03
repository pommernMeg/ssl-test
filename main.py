#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ssl-test.py: Description of what foobar does."""

__author__      = "Marcel Eggert"
__copyright__   = "Copyright 2021, Heinlein-Support"
__version__ = "0.0.1"

import sslTester
import helptools

def main():
    import argparse
    import sys
    
    if helptools.git_pull_change("/home/marcel/Dokumente/Arbeit/tool-box/ssl-test"):
        print("Es gibt eine Updates im git repo")
        
    parser = argparse.ArgumentParser()

    parser.add_argument('--mx',
                        dest='mx',
                        action='store_true',
                        default=False,
                        help='get mx records and start the ssl tests for it')

    args = parser.parse_args()

    if args.mx:
        self.mx = True
    
    args_dict = vars(args)
    print(len( vars(args) ) )
    
    ssl = sslTester.sslTester()
    ssl.loadBanner()
    ssl.hostInfos()

if __name__ == '__main__':
    main()
