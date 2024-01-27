#Script para testar se a recepção do radar está ok

import socket
import struct

def receive_multicast(group_ip, port, buffer_size=1024):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Allow multiple sockets to use the same PORT number
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the port that we know will receive multicast data
    sock.bind(('', port))

    # Tell the kernel that we are a multicast socket
    mreq = struct.pack("4sl", socket.inet_aton(group_ip), socket.INADDR_ANY)

    # Add the socket to the multicast group
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Receive data
    while True:
        print("Waiting for data...")
        data, addr = sock.recvfrom(buffer_size)
        print(f"Data received from {addr}: {data}")

if __name__ == "__main__":
    group_ip = '236.6.7.8'  # Replace with your multicast group IP
    port = 6678  # Replace with your multicast port

    receive_multicast(group_ip, port)
