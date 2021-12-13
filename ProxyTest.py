import urllib.request as urllib2
import socks
from sockshandler import SocksiPyHandler
from Colors import green, red
from Time import getMillis

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