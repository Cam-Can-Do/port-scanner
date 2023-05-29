import sys
import socket

# returns true if the specified port on the host network is open
# returns false if it is closed
def portOpen(hostIP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        if s.connect_ex((hostIP, port)):
            return False
        else:
            return True
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
    finally: 
        s.close()

# scans ports over the specified range and prints results
def scanPorts(hostIP, start_port, end_port):
    for port in range(start_port, end_port + 1):
        result = portOpen(hostIP, port)
        printResult(port, result)

# prints whether a port is open or closed (depending on commented lines)
def printResult(port, result):    
    # Only print open ports
    if result:
        print(f"Port {port} is open.")

    # Print closed and open ports
    # print(f"Port {port} is", ("open." if result else "closed."))

def main():
    # incorrect usage check and message
    if len(sys.argv) < 3:
        print("Usage: python3 portscanner.py <host> <port(s)>")
        sys.exit(1)

    # get hostname, which is the second argument and its IP
    host = sys.argv[1]
    hostIP = socket.gethostbyname(host)

    # remaining arguments are port range(s) to scan
    ports = sys.argv[2:]
    for port in ports:
        # check if a range, indicated by containing a "-"
        if "-" in port:
            start_port, end_port = map(int, port.split("-"))
            scanPorts(hostIP, start_port, end_port)
        else:
            scanPorts(hostIP, int(port), int(port))

if __name__ == "__main__":
    main()
