import socket
import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Video Server')
parser.add_argument('--tcp', action='store_true', help='Use TCP protocol')
parser.add_argument('--udp', action='store_true', help='Use UDP protocol')
parser.add_argument('--cmd', type=str, default="mplayer -fps 25 -cache 512 -", help='Command for mediaplayer')
args = parser.parse_args()

# mediaplayer cmd command
cmd_mplayer = args.cmd
mprocess = subprocess.Popen(cmd_mplayer, shell=True, stdin=subprocess.PIPE)

# Port des Servers
PORT = 5000

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


# Maximale Anzahl der Verbindungen in der Warteschlange
backlog = 1

# Erstellen eines Socket (TCP und UDP)
sock = socket.socket(address_family, socket_type)
sock.bind(('', PORT))

# Lausche am Socket auf eingehende Verbindungen (Nur TCP)
if args.tcp:
	sock.listen(backlog)
	clientsocket, address  = sock.accept()

# Daten (der Groesse BUFFER_SIZE) aus dem Socket holen, ausgeben und zuruecksenden:
while True:
    # TCP:
	if args.tcp:
		data = clientsocket.recv(BUFFER_SIZE)
		print(data)

    # UDP:
	if args.udp:
		data, address = sock.recvfrom(BUFFER_SIZE)
		print(data)

	mprocess.stdin.write(data)