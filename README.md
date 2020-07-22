# Echo

This program uses UDP sockets, there are two scripts, 'client.py' and 'server.py'. 
The program lets the client send a string of some specified length to the server 
over the network, and the server simply echoes back that string back to the client.

The client program should take the following command-line parameters:
• IP address of server
• UDP port of server
• Length of string to be sent

The client program reads in the above input parameters, initialize a string containing
alphabetical characters of the specified length, and send the message using the UDP socket API
to the server running at the specified IP address and port. If the client does not receive a
message back from the server within a certain amount of time (one second), the client should
retry up to a maximum number of tries (3) before terminating.2 The program output should
print out trace information when data is sent and received, and account for error conditions.