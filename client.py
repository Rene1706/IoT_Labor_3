import socket
import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Video Streaming')
parser.add_argument('--tcp', action='store_true', help='Use TCP protocol')
parser.add_argument('--udp', action='store_true', help='Use UDP protocol')
parser.add_argument('--cmd', type=str, default="raspivid -t 0 -fps 20 -w 1280 -h 720 -b 2000000 -o -", help='Command for raspivid')
args = parser.parse_args()

# IP und Port des Servers
IP = '172.23.x.x'
PORT = 5000

# raspivid cmd command
cmd_raspivid = args.cmd
rasprocess = subprocess.Popen(cmd_raspivid, shell=True, stdout=subprocess.PIPE)

# Lesepuffergroesse
BUFFER_SIZE = 1400

# Unterstuetzte Addresstypen (IPv4, IPv6, lokale Addressen)
address_families = (socket.AF_INET, socket.AF_INET6, socket.AF_UNIX)

# Unterstuetzte Sockettypen (TCP, UDP, Raw (ohne Typ))
socket_types = (socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)

# Passenden Address- und Sockettyp waehlen
address_family = address_families[0]
if args.tcp:
    socket_type = socket_types[0]
elif args.udp:
    socket_type = socket_types[1]
else:
    raise ValueError("Please specify either --tcp or --udp")

# Erstellen eines Sockets (TCP und UDP)
sock = socket.socket(address_family, socket_type)

# Verbinden zu einem Server-Socket (Nur TCP)
if args.tcp:
    sock.connect((IP,PORT))

# Sende immer wieder "Hello" an den Server
while True:
    message = "Hello"
        
    # TCP
    if args.tcp:
        sock.send(message.encode())
        	
    # UDP
    if args.udp:
        sock.sendto(message.encode(), (IP, PORT))