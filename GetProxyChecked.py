import os
import time
from typing import Callable
import random
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
    def __init__(self, ip:str, port:int):
        self.ip = ip
        self.port = port
    
    def test(self) -> dict:
        init_time = getMillis()
        opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, self.ip, self.port))

        try:
            ret = opener.open("https://api.ipify.org/")
            
            return {
                'ip': self.ip,
                'port': str(self.port),
                'time': getMillis()-init_time,
                'status': True
            }
        except Exception:
            return {
                'ip': self.ip,
                'port': str(self.port),
                'time': 0,
                'status': False
            }

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
    
    def get(self, limit:int, postTest:Callable=None) -> list:
        yellow(f"\n\t{self.ips_total} IPs in list\n")

        good_ips = []

        ini_post = random.randint(0, self.ips_total-1)

        for index in range(self.ips_total):
            if (len(good_ips) >= limit):
                break
            
            indexPos = (index+ini_post)%self.ips_total
            ipRaw = self.ips[indexPos]
            ip = ipRaw.split(":")[0]
            port = int(ipRaw.split(":")[1])

            test = ProxyS5Test(ip, port).test()
            pTest = True

            if postTest is not None:
                pTest = postTest(test)

            perc = "{:.3f}".format((index+1)/self.ips_total)
            perc = f"{perc}%"

            if (test['status'] and pTest):
                green(f"{perc}\tGood proxy\t{test['ip']}:{test['port']}\t{test['time']}ms")
                good_ips.append(test)

        return good_ips