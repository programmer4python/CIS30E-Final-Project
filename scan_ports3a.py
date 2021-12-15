import socket
from threading import *
import time
import ipaddress

threads=[]

global ip
with open('ip.txt') as f:
    ip = f.readline()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("That is not a valid IP address.")
f.close()

def connect(ip_add_entered,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.05)
            if s.connect((ip_add_entered,port)):
                pass
            else:
                try:
                    print("{}: {} tcp open service {}".format(ip_add_entered,port,getservbyport(port,'tcp')))
                except OSError as error:
                    print("{}: {} tcp open service not found for this port".format(ip_add_entered,port))
    except:
        pass

def scan_ports(ip_add_entered, min_port, max_port):
    start=time.time()

    for port in range(min_port, max_port):
        port_thread = Thread(target=connect, args=(ip_add_entered,port))
        port_thread.start()
        threads.append(port_thread)

    for thread in threads:
        thread.join()
    print("All ports scanned.")
    end=time.time()
    time_e = end - start
    print("Time to execute: ", round(time_e,2)," seconds")
if __name__ == '__main__':
    scan_ports(ip,1,65535)

