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
        
        path, version, info = self.check_openssl_version()
        if len(info) == 0:
            print(f"""#
#  IPv4: {values['ipinfo'][1]['ip']} \t IPv6: {values['ipinfo'][0]['ip']} 
#  hostname:  {socket.gethostname()}             
#  
#  OpenSSL 
#  path: {path} \tversion: {version} 
#  """)
            self.separatorLine()
        else:
            print(f"""#
#  IPv4: {values['ipinfo'][1]['ip']} \t IPv6: {values['ipinfo'][0]['ip']} 
#  hostname:  {socket.gethostname()}             
#  
#  OpenSSL 
#  path: {path} \tversion: {version} 
#
#  {info}
#  """)
            self.separatorLine()
    
    def check_openssl_version(self):
        from subprocess import check_output
        from packaging.version import Version, LegacyVersion
        import re
        
        path = str(check_output(["which", "openssl"]).decode("utf-8")).replace("\n","")
        
        version = str(check_output([path, "version"]).decode("utf-8")).replace("\n","")
        
        vers1 = re.sub("[^0-9.]+", "", version.split(" ")[1])
        vers2 = re.sub("[^0-9.]+", "", self.openssl_local_version)
        
        if Version(vers1) < Version(vers2):
            info = "Bitte Version aus lib Verzeichnis nutzen"
        else:
            info = ""
            
        return path, version, info
        
    def loadConfig(self):
        var =""
    
    def loadColor(self):
        var =""