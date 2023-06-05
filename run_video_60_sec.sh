#!/bin/bash

#Run tcpdump to sniff tcp traffic
sudo tcpdump -n -i enp3s0 tcp -w server.pcap &

# Save the process ID (PID) of the tcpdump process
pid_tcpdump=$!

# Run the Python script in the background
python server.py --tcp &

# Save the process ID (PID) of the Python script
pid_python=$!

#ssh pi@192.168.0.55 "/home/pi/IoT/Labor_3/run_video_60_sec.sh"
# Sleep for 60 seconds
sleep 70

# Kill the Python script using the PID
kill -9 $pid_python
# Kill tcpdump process
kill -9 $pid_tcpdump
