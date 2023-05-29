import socket
import subprocess
import sys
from datetime import datetime

def portOpen(hostIP, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(5)

        if s.connect_ex((hostIP, port)):
            return False
        else:
            return True
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    

def scanAll(hostIP):

    # starting datetime
    t1 = datetime.now()

    for port in range(1, 5000):
        result = portOpen(hostIP, port)
        printResult(port, result)
        #s.close()


    #check end datetime
    t2 = datetime.now()

    total = t2 - t1

    print("Scanning Completed in: ", total)

def printResult(port, result):
    print(f"Port {port} is", ("open." if result else "closed."))



def main():
    '''
    # clear terminal screen
    subprocess.call('clear', shell=True)
    '''

    # input
    host = input("Remote host to scan: ")
    hostIP = socket.gethostbyname(host)

    #port = int(input("Port to scan: "))


    #subprocess.call('clear', shell=True)

    # print banner with information
    #print("_" * 60) 
    #print(f"Scanning remote host {hostIP} on port {port}")
    #print("-" * 60) 

    scanAll(hostIP)
'''
    # starting datetime
    t1 = datetime.now()

    try:
        for port in range(1, 5000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((remoteServerIP, port))
            if result == 0:
                print (f"Port {port}:    Open")
            sock.close()


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
'''

if __name__ == "__main__":
    main()