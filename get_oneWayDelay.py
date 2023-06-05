from collections import defaultdict

def calculate_one_way_delay(client_file, server_file, output_file):
    # Read the client.txt file
    client_data = []
    with open(client_file, 'r') as file:
        for line in file:
            timestamp, _, _, sequence_number = line.split('\t')
            client_data.append((float(timestamp), int(sequence_number)))

    # Read the server.txt file
    server_data = []
    with open(server_file, 'r') as file:
        for line in file:
            timestamp, _, _, sequence_number = line.split('\t')
            server_data.append((float(timestamp), int(sequence_number)))

    # Calculate one-way delay for each sequence number
    one_way_delays = []
    for server_entry in server_data:
        server_timestamp, sequence_number = server_entry
        client_timestamp = next((client_entry[0] for client_entry in client_data if client_entry[1] == sequence_number), None)
        if client_timestamp is not None:
            one_way_delay = server_timestamp - client_timestamp
            one_way_delays.append((sequence_number, one_way_delay))

    # Write the one-way delays to the output file
    with open(output_file, 'w') as file:
        for sequence_number, one_way_delay in one_way_delays:
            pass
	    #file.write(f"{sequence_number},{one_way_delay}\n")


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
