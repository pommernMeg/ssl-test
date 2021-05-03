class sslTester():
    """
    Create ssl Tester module for testing ssl connections.
    1. config aus yaml laden
    2. Farben fürs Terminal laden
    
    """
   
    def __init__(self):
        openssl_local_path = "/usr/local/bin/openssl"
        openssl_local_version = "1.1.1k"
        build_version = "0.0.1"
        build_date = "03/05/2021"

    def separatorLine(self):
        print(f"####################################################################")
              
    def loadBanner(self):
        self.separatorLine()
        print(f"""#           _         _             _                             
#   ___ ___| |  ___  | |_  ___  ___| |_  ___  _ _      _ __  _  _ 
#  (_-<(_-<| | |___| |  _|/ -_)(_-<|  _|/ -_)| '_|  _ | '_ \| || |
#  /__//__/|_|        \__|\___|/__/ \__|\___||_|   (_)| .__/ \_, |
#                                                     |_|    |__/ 
#              """)
        self.separatorLine()
        print(f"""#  
#              Inspired by https://testssl.sh/
#              """)
        self.separatorLine()
    def hostInfos(self):
        import socket
        import requests
        import json
        import urllib
        
        url = 'http://checkip4.spdyn.de/json'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data) 

        print(f"""#
#  IPv4: {values['ipinfo'][1]['ip']} \t IPv6: {values['ipinfo'][0]['ip']} 
#  hostname:  {socket.gethostname()}             
#  
#  openssl path: {dd} \topenssl version: {ss} 
#  """)
        self.separatorLine()
    
    def check_openssl_version(self):
        import subprocess
        
        subprocess.call(["ls", "-l"])
        
    def loadConfig(self):
        var =""
    
    def loadColor(self):
        var =""