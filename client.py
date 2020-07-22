#! /usr/bin/env python3
# Echo Client
"""
Programming language and version: Python 3.8.1
Testing Environment:
    OS: Windows
    IDE with entrance file: N/A
    Command Lines:
        python client.py 127.0.0.1 12000 10
"""

import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count  # Initialize data to be sent

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(3):
    # Send data to server
    print("Sending data to   " + host + ", " + str(port) + ": " + data)
    clientsocket.sendto(data.encode(), (host, port))
    try:
        # Receive the server response
        clientsocket.settimeout(1)
        dataEcho, address = clientsocket.recvfrom(count)
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break
    except OSError:
        print("Message timed out")

# Close the client socket
clientsocket.close()