from ProxyTest import ProxyS5Test
from Colors import yellow

class GetProxyChecked:
    def __init__(self) -> None:
        self.file_ips = open("ips.txt", "r").read()
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