#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", dest="interface", help="Enter interface")
options = parser.parse_args()

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 21")

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
     print(packet.show())

sniffer(str(options.interface))