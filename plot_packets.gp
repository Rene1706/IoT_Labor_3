#set xdata time
#set timefmt "%s%3f"
#set format x "%.3f ms"
set logscale x
set xlabel "Time"
set ylabel "Packet Count"
set title "Total Video Packets Sent and Received"
set grid

plot "client_packet_count.txt" using 1:2 with lines title "Client Packets", \
     "server_packet_count.txt" using 1:2 with lines title "Server Packets"

pause -1
