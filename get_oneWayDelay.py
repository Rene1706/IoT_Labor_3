from collections import defaultdict
import numpy as np
def calculate_one_way_delay(client_file, server_file, output_file):
    # Read the client.txt file
    client_data = []
    server_data = []

    with open("client_packet_count.txt", 'r') as file:
        for line in file:
            timestamp, sequence_number = line.strip().split('\t')
            client_data.append((float(timestamp), int(sequence_number)))

    # Read the server.txt file
    server_data = []
    with open("server_packet_count.txt", 'r') as file:
        for line in file:
            timestamp, sequence_number = line.strip().split('\t')
            server_data.append((float(timestamp), int(sequence_number)))

    one_way_delays = []
    # Calculate one-way delay for each sequence number
    for client_entry in client_data:
        client_timestamp, client_sequence_number = client_entry
        for server_entry in server_data:
            server_timestamp, server_sequence_number = server_entry
            if server_sequence_number == client_sequence_number:
                one_way_delays.append(client_timestamp-server_timestamp)
                break
    #print(one_way_delays)
    print("MEAN:", np.mean(one_way_delays[:4000]))
    print("STD:", np.std(one_way_delays[:4000]))
    return one_way_delays


def calculate_packet_counts(client_file, server_file, output_file):
    client_counts = [(0,0)]
    server_counts = [(0,0)]
    # Read client.txt file and count client packets
    with open(client_file, 'r') as file:
        for line in file:
            c_timestamp, _, _, c_seq = line.split()
            if c_seq != "1":
                client_counts.append((c_timestamp, c_seq))

    # Read server.txt file and count server packets
    with open(server_file, 'r') as file:
        for line in file:
            s_timestamp, _, _, s_seq = line.split()
            if c_seq != "1":
                server_counts.append((s_timestamp, s_seq))
    del server_counts[0]
    del client_counts[0]
    print(len(server_counts))
    print(len(client_counts))
    # Write packet counts to output file
    with open("server_packet_count.txt", 'w') as file:
        for item in server_counts:
            file.write(f"{item[0]}\t{item[1]}\n")
    with open("client_packet_count.txt", 'w') as file:
        for item in client_counts:
            file.write(f"{item[0]}\t{item[1]}\n")


# Specify the input file paths and output file path
client_file = 'client.txt'
server_file = 'server.txt'
output_file = 'packet_counts.txt'

# Call the function to calculate packet counts and write to the output file
calculate_packet_counts(client_file, server_file, output_file)

# Specify the input file paths and output file path
client_file = 'client.txt'
server_file = 'server.txt'
output_file = 'oneWayDelays.txt'

# Call the function to calculate one-way delays and write to the output file
calculate_one_way_delay(client_file, server_file, output_file)
