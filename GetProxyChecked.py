import os
import time
import urllib.request as urllib2
import socks
from sockshandler import SocksiPyHandler
from termcolor import cprint

def green(s) -> str:
    cprint(s, 'green')

def red(s) -> str:
    cprint(s, 'red')

def yellow(s) -> str:
    cprint(s, 'yellow')

def getMillis() -> int:
    milli = int(round(time.time() * 1000))
    return milli
class ProxyS5Test:
    def __init__(self, ip:str, port:int, display_only_good:bool=False):
        self.ip = ip
        self.port = port
        self.dog = display_only_good
    
    def test(self, index=None, total=None) -> bool:
        init_time = getMillis()
        opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, self.ip, self.port))

        if (index != None and index != None):
            perc = round((index+1)/total, 3)
            perc = "{:.3f}".format(perc)
            perc = f"{str(perc)}%"
        else:
            perc = ""

        try:
            ret = opener.open("https://api.ipify.org/")
            green(f"{perc}\tGood proxy\t{self.ip}:{str(self.port)}\t{str(getMillis()-init_time)}ms")
            return True
        except Exception:
            if not self.dog:
                red(f"{perc}\tBad Proxy\t{self.ip}:{str(self.port)}")
            return False

def getIpsFilePath() -> str:
    return os.path.abspath("ips.txt")
class GetProxyChecked:
    def __init__(self, list_file:str=None) -> None:
        if (list_file is None):
            self.file_ips = open(getIpsFilePath(), "r").read()
        else:
            self.file_ips = open(list_file, "r").read()
        self.ips = self.file_ips.split("\n")
        self.ips_total = len(self.ips)
    
    def get(self, limit) -> list:
        yellow(f"\n\t{self.ips_total} IPs in list\n")

        good_ips = []

        for index in range(self.ips_total):
            if (len(good_ips) >= limit):
                break

            ipRaw = self.ips[index]
            ip = ipRaw.split(":")[0]
            port = int(ipRaw.split(":")[1])

            test = ProxyS5Test(ip, port, display_only_good=True).test(index, self.ips_total)

            if (test):
                good_ips.append(ipRaw)

        return good_ips