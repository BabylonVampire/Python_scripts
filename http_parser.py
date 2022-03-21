import scapy.all as scapy
from scapy.layers import http

print("Enter interface:")
interface = str(input())

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
     print(packet.show())

sniffer(str(interface))
