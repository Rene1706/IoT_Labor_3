#!/bin/bash

# Step 1: Get the file client.pcap from the remote Raspberry Pi using scp
#scp pi@172.23.90.35:/home/pi/Documents/IoT_Labor_3/client.pcap /home/student/Documents/Group03/IoT_Labor_3/

# Step 2: Process .pcap files into .txt files with sequence number and timestamp
tshark -r client.pcap -Y "tcp.flags == 0x010 && ip.src == 172.23.90.35 && ip.dst == 172.23.90.112" -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.seq > client.txt
tshark -r server.pcap -Y "tcp.flags == 0x010 && ip.src == 172.23.90.35 && ip.dst == 172.23.90.112" -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.seq > server.txt

#tshark -r client.pcap -Y "tcp.flags == 0x010 && ip.addr == 172.23.90.35" -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.seq > client.txt
#tshark -r server.pcap -Y "tcp.flags == 0x010 && ip.addr == 172.23.90.35" -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.seq > server.txt

# Step 3: Execute the Python script get_oneWayDelay.py
python3 get_oneWayDelay.py

# Step 4: Use gnuplot to plot the file oneWayDelay.txt
gnuplot plot_packets.gp
#gnuplot -e "plot '/path/to/local/destination/oneWayDelay.txt' with lines"

