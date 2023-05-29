import socket
import subprocess
import sys
from datetime import datetime

# Blank screen
subprocess.call('clear', shell=True)

# input
remoteServer = input("Remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print (remoteServer)
print (remoteServerIP)

# print banner with information
print("_" * 60) 
print("Scanning remote host ", remoteServerIP)
print("-" * 60) 

# starting datetime
t1 = datetime.now()

try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print (f"Port {port}:    Open")
        sock.close()

except KeyboardInterrupt:
    print("\nStopped by Keyboard Interrupt")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#check end datetime
t2 = datetime.now()

total = t2 - t1

print("Scanning Completed in: ", total)