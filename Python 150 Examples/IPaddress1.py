import socket
hostname = "thepcgames.net"
try:
    IPAddr = socket.gethostbyname(hostname)
    print("IP Address of this website is: " +IPAddr)

except socket.gaierror:
    print("The website doesn't exist")