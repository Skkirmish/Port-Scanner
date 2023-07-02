import socket

for port in range(5000, 5004):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("192.168.0.250", port))

    if result == 0:
        print("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")