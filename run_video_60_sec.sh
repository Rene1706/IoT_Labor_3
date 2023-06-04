#!/bin/bash

#Run tcpdump to sniff tcp traffic
sudo tcpdump -n -i eth0 tcp -w client.pcap &

# Save the process ID (PID) of the tcpdump process
pid_tcpdump=$!

# Run the Python script in the background
python client_1.py --tcp &

# Save the process ID (PID) of the Python script
pid_python=$!

# Sleep for 60 seconds
sleep 60

# Kill the Python script using the PID
kill -9 $pid_python
# Kill tcpdump process
kill -9 $pid_tcpdump