from ProxyTest import ProxyS5Test
from Colors import yellow
from Output import Output
from Time import getMillis

file_ips = open("ips.txt", "r").read()
ips = file_ips.split("\n")
ips_total = len(ips)

yellow(f"\n\t{ips_total} IPs in file\n")

good_out = Output(f"good_{getMillis()}")
bad_out = Output(f"bad_{getMillis()}")

for index in range(ips_total):
    ipRaw = ips[index]
    ip = ipRaw.split(":")[0]
    port = int(ipRaw.split(":")[1])

    test = ProxyS5Test(ip, port).test(index, ips_total)

    if (test):
        good_out.write(ipRaw)
    else:
        bad_out.write(ipRaw)

good_out.close()
bad_out.close()