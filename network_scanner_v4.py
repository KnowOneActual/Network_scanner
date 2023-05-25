from scapy.all import ARP, Ether, srp

# create ARP request packet
arp = ARP(pdst="10.100.10.0/24")

# create Ether broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# combine packets
packet = ether/arp

# send and receive packets
result = srp(packet, timeout=3, verbose=0)[0]

# list of clients
clients = []

# iterate through received packets
for sent, received in result:
    # append client's MAC and IP address to list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print list of clients
print("Network clients found:")
print("IP address\tMAC address")
for client in clients:
    print(f"{client['ip']}\t{client['mac']}")
