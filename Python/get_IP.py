import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"My IP Address is {ip_address}")