#!/usr/bin/env python

import scapy.all as scapy
import re
import subprocess

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast/arp_request
    answered = scapy.srp(request, timeout=1, verbose=False)[0]
    _list = []
    for i in answered:
        alphabet = {"mac" : str(i[1].hwsrc), "ip" : str(i[1].psrc)}
        _list.append(alphabet)
    return _list

def print_results(list_of):
    print("IP\t\t\tMAC\n---------------------------------")
    for i in list_of:
        print(str(i["ip"]) + "\t\t" + str(i["mac"]))

my_ip = re.findall(r"\d+.\d+.\d+.\d+", str(subprocess.check_output("route -n", shell=True)))
try:
    print_results(scan(str(my_ip[3]) + "/24"))
except:
    print("[-] Connection Error. Please, check your internet connection.")
