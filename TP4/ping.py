from scapy.all import *

ping = ICMP(type=8)
packet = IP(src="10.33.77.246/2", dst="passerelle_adresse_IP")
frame = Ether(src="98:3b:8f:b4:db:38", dst="passerelle_MAC_dst")
final_frame = frame/packet/ping

answers, unanswered_packets = srp(final_frame, timeout=10)

print(f"Pong reçu : {answers[0]}")
