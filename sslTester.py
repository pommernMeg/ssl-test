#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""sslTester.py: """

__author__ = "Marcel Eggert"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"


class sslTester():
    """
    Create ssl Tester module for testing ssl connections.
    1. config aus yaml laden
    2. Farben fürs Terminal laden

    """

    def __init__(self):
        self.openssl_local_path = "/usr/local/bin/openssl"
        self.openssl_local_version = "1.1.1k"
        self.build_version = "0.0.1"
        self.build_date = "03/05/2021"
        self.news = ""
        self.CONFIG = {}
        self.begin_test = ""
        self.end_test = ""

    def initial(self):
        import helptools

        self.CONFIG = helptools.loadConfig()

        status, news = helptools.git_pull_change(self.CONFIG['GIT_REPO_PATH'])

        if status:
            self.loadBanner(__version__, news)
        else:
            self.loadBanner(__version__, news)
        self.hostInfos()

    def loadBanner(self, version, news):
        import helptools

        helptools.separatorLine()
        print(f"""#           _         _             _                             
#   ___ ___| |  ___  | |_  ___  ___| |_  ___  _ _      _ __  _  _ 
#  (_-<(_-<| | |___| |  _|/ -_)(_-<|  _|/ -_)| '_|  _ | '_ \| || |
#  /__//__/|_|        \__|\___|/__/ \__|\___||_|   (_)| .__/ \_, |
#                                                     |_|    |__/ 
#   v{version} {news}
# """)
        helptools.separatorLine()
        print(f"""#  
#              Inspired by https://testssl.sh/
#              """)
        helptools.separatorLine()

    def hostInfos(self):
        import socket
        import requests
        import json
        import urllib
        import helptools

        url = 'http://checkip4.spdyn.de/json'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        ipv4 = json.loads(data)

        url = 'http://checkip6.spdyn.de/json'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        ipv6 = json.loads(data)

        path, self.version, self.info = self.check_openssl_version()
        if len(self.info) == 0:
            print(f"""#
#  IPv4: {ipv4['ipinfo'][1]['ip']} \t IPv6: {ipv6['ipinfo'][1]['ip']} 
#  hostname:  {socket.gethostname()}             
#  
#  OpenSSL 
#  path: {path} \tversion: {self.version} 
#  """)
            helptools.separatorLine()
        else:
            print(f"""#
#  IPv4: {ipv4['ipinfo'][1]['ip']} \t IPv6: {ipv6['ipinfo'][0]['ip']} 
#  hostname:  {socket.gethostname()}             
#  
#  OpenSSL 
#  path: {path} \tversion: {self.version} 
#
#  {self.info}
#  """)
            helptools.separatorLine()

    def check_openssl_version(self):
        from subprocess import check_output
        from packaging.version import Version, LegacyVersion
        import re

        path = str(check_output(["which", "openssl"]).decode(
            "utf-8")).replace("\n", "")

        version = str(check_output([path, "version"]).decode(
            "utf-8")).replace("\n", "")

        vers1 = re.sub("[^0-9.]+", "", version.split(" ")[1])
        vers2 = re.sub("[^0-9.]+", "", self.openssl_local_version)

        if Version(vers1) < Version(vers2):
            info = "Bitte Version aus lib Verzeichnis nutzen"
        else:
            info = ""

        return path, version, info

    def loadColor(self):
        var = ""

    def start_check(self, record):
        from datetime import datetime
        import helptools

        self.begin_test = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Testing now (2021-05-04 16:37) ---> 82.165.229.87:443 (gmx.net) <---
        print(f"""#
#   Begin test {self.begin_test} ------------------> {record}""")
        helptools.separatorLine()

    def host_lookup(self, domain, mx=False):
        import dns.resolver
        import helptools

        prio_filter = True
        address = []
        print(f"""#
#               domain: {domain}
#               MX Abfrage: {mx}
#""")
        if not mx:
            records = dns.resolver.resolve(domain, "A")
            for rec in records:
                print(f"#               IPv4: {rec.address}")
                address.append(rec.address)
            records = dns.resolver.resolve(domain, "AAAA")
            for rec in records:
                print(f"#               IPv6: {rec.address}")
                address.append(rec.address)
        else:
            temp = []
            for rec in dns.resolver.resolve(domain, "MX"):
                temp.append(rec.to_text())

            if prio_filter:
                prio = 1000
                for item in temp:
                    addr = item.split(" ")
                    if prio > int(addr[0]):
                        prio = int(addr[0])

                print(f"""#                     Records
#               Priority\t|\tIP
#               ----------------+----------------------------""")
                for item in temp:
                    addr = item.split(" ")
                    if prio == int(addr[0]):
                        print(f"""#               \t{addr[0]}\t|\t{addr[1]}""")
                        address.append(self.get_host_ip(addr[1]))
            else:
                for item in temp:
                    addr = item.split(" ")
                    address.append(self.get_host_ip(addr[1]))

        print(f"""#""")
        helptools.separatorLine()

        return address

    def get_host_ip(self, domain):
        import dns.resolver

        records = []
        records4 = dns.resolver.resolve(domain, "A")
        records6 = dns.resolver.resolve(domain, "AAAA")

        records.append(records4[0].address)
        records.append(records6[0].address)

        return records
