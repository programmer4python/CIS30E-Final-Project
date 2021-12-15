import multiprocessing
import time
import socket
import ipaddress


open_ports = []

port_min = 1
port_max = 65535

global ip
with open('ip.txt') as f:
    ip = f.readline()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(len(ip))
        print("That is not a valid IP address.")
f.close()

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id
    def run(self):
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.05)
                    s.connect(ip, port)
                    open_ports.append(port)
            except:
                pass

        for port in open_ports:
            try:
                protocolname = 'tcp'
                print(f"Port {port} is open on {ip}.")
                print("Port: %s => service name: %s" %(port, socket.getservbyport(port,protocolname)))
            except OSError as error:
                print(f"Service not found for port {port}")

if __name__ == '__main__':
    start = time.time()
    processes = Process(1), Process(2), Process(3), Process(4)

    for p in processes:
        p.start()
        p.join()
    end = time.time()
    time_e = end - start
    print("Time to execute: ", round(time_e,2))
    if len(open_ports) == 0:
        print("No open ports.")
