#!/usr/local/bin/python3

import glob
import re
from ipaddress import IPv4Interface

def case_construction (str):
    m1 = re.match("^interface (.+)", str)
    if m1:
        return {"int":m1.group(1)}
    m2 = re.match("^hostname (.+)", str)
    if m2:
        return {"host":m2.group(1)}
    m3 = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", str)
    #    m1=re.match('^ ip address ((?:[0-255].){3}[0-255])',str)
    if m3:
        print(m3.group(1))
        return {"ip":IPv4Interface(str(m3.group(1)) + "/" + str(m3.group(2)))}

    return ("UNCLASSIFIED",)

ipaddr = []
interfaces = []
hosts = []

for file in glob.glob('C:\\Users\\mn.danilin\\Downloads\\config_files\\cod-asw1_10.12.225.52.txt'):
    f=open(file)
    for iter_str in f:
        result = case_construction(iter_str)
        if "ip" in result:
            ipaddr.append(result)
        if "int" in result:
            interfaces.append(result)
        if "host" in result:
            hosts.append(result)

print(ipaddr)
print(interfaces)
print(hosts)



