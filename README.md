## Project title: Port Scanner
## Project Description: A python script for scanning and finding open ports for a specific IP address

 The python script command is:
```
port_scanner.py [ip address] or [hostname]
```
A port is a logical construct assigned to network processes so that they can be identified within the system.
We can't acces ports directly, this is the main reason we need sockets.
A socket is what a program or a service binds to, it will include an IP address and a PORT number.It is used to identify both a machine and a service within the machine.
Both socket and port are terms used in the **Transport layer** from the OSI Model

I used the sys python module to manipulate the script terminal arguments.The documentation for the module can be found here:
https://docs.python.org/3/library/sys.html#sys.argv

The .argv function stores the command introduced in the terminal window
```
port_scanner.py [ip]
where
argv[0] = port_scanner.py
argv[1] = [ip]
```
I also made use of the socket module, to connect a PORT and an IP address together.
The documentation for the module can be found here: 
https://docs.python.org/3/library/socket.html

The gethostbyname() function transforms the host name into an IP address using the DNS lookup process.
The process of finding the IP address is achieved by searching the DNS (Domain Name Servers) until a match on the domain name is found.

In the socket function, AF_INET is an IPV4 address, and SOCK_STREAM is a PORT number.

The s.connect_ex() function returns an error indicator, if a port is open, there a connection is possible and the function is returning a 0.Otherwise, if the port is not open, the function returns a 1

In this project I also implemented some Interruption actions for exiting the program.
