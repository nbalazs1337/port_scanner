#!/urs/bin/env python

import socket
import sys
from datetime import datetime
#Defining target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 port_scanner.py <ip>")


print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))#return an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
        print("\n Exiting program")
        sys.exit()
except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
except socket.error:
        print("Couldn't connect to server")
        sys.exit()
