from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        if TCP in packet:
            proto_name = "TCP"
            payload = packet[TCP].payload
        elif UDP in packet:
            proto_name = "UDP"
            payload = packet[UDP].payload
        else:
            proto_name = "Other"
            payload = packet[IP].payload
        
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto_name}")
        print(f"Payload: {payload}")
        print("-" * 50)

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if _name_ == "_main_":
    main()
