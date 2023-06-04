set xlabel "Time"
set ylabel "Packet Count"
set title "Total Video Packets Sent and Received"
set grid

plot "packet_counts.txt" using 1:2 with lines title "Client Packets", \
     "packet_counts.txt" using 1:3 with lines title "Server Packets"

pause -1