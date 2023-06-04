import socket

# IP und Port des Servers
IP = '172.23.x.x'
PORT = yyyy

# Lesepuffergroesse
BUFFER_SIZE = 1400

# Unterstuetzte Addresstypen (IPv4, IPv6, lokale Addressen)
address_families = (socket.AF_INET, socket.AF_INET6, socket.AF_UNIX)

# Unterstuetzte Sockettypen (TCP, UDP, Raw (ohne Typ))
socket_types = (socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)

# Passenden Address- und Sockettyp waehlen
address_family = address_families[0]
socket_type = socket_types[0]

# Erstellen eines Sockets (TCP und UDP)
sock = socket.socket(address_family, socket_type)

# Verbinden zu einem Server-Socket (Nur TCP)
sock.connect((IP,PORT))

# Sende immer wieder "Hello" an den Server
while True:
    message = "Hello"
        
    # TCP
    sock.send(message)
        	
    # UDP
    sock.sendto(message, (IP, PORT))