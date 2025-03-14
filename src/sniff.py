from scapy.all import sniff, IP

INTERFACE = "en0" 

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"Packet: {packet[IP].src} -> {packet[IP].dst}")

sniff(prn=packet_callback, store=0, iface=INTERFACE)
