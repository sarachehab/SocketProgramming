import socket
import time

# the server name and port client wishes to access
server_name = 'localhost'
server_port = 11000
# create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP client running...")
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)

# send the message to the udp server
for i in range(10):
    msg = 10*i + 5
    client_socket.sendto(msg, (server_name, server_port))
    time.sleep(400)

# return values from the server
msg, sadd = client_socket.recvfrom(2048)

# show output and close client
print(msg.decode())
client_socket.close()
