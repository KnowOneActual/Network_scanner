# Network_scanner
<h1 align="center" id="title">Netowrk scanner python script</h1>

<p id="description">A Python script use scan devices on at network</p>

this code is a simple network scanner that uses the scapy library to send ARP requests to all devices on the network. The ARP request packet asks the device to respond with its MAC address. The scapy library will then return a list of all the devices that responded, along with their IP and MAC addresses.

The code first imports the ARP, Ether, and srp modules from the scapy library.

The next step is to create the ARP request packet. The ARP class has a pdst attribute that specifies the destination IP address. In this case, the destination IP address is set to 10.100.10.0/24, which represents the entire 10.100.10.0 subnet.

The next step is to create the Ether broadcast packet. The Ether class has a dst attribute that specifies the destination MAC address. In this case, the destination MAC address is set to the broadcast MAC address, which is ff:ff:ff:ff:ff:ff.

The next step is to combine the ARP request packet and the Ether broadcast packet into a single packet. This is done using the / operator.

The next step is to send the packet and receive the responses. The srp() function sends the packet and waits for a response. The timeout parameter specifies the number of seconds to wait for a response. The verbose parameter specifies whether to print debug messages.

The next step is to create a list of clients. The clients list will store the IP and MAC addresses of all the devices that responded to the ARP request.

The next step is to iterate through the received packets. For each packet, the code will append the device's IP and MAC addresses to the clients list.

The final step is to print the list of clients. The code will print the IP address and MAC address of each device, one per line.

<h2>🛡️ License:</h2>

This project is licensed under the MIT
