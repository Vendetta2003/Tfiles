import socket
import threading
import time 
from threading import *
import os



def main():
    def scan(ip , port):# 192.168.0.1 , 23-56
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        resp = s.connect_ex((ip , port))
        if(resp == 0):
              print(f"[+] Port {port} is up")
        else:
              print(f"[-] Port {port} is down")
        
    os.system("cls")     
    ip = input("Enter IP addr :- ")
    args = input("Enter PORT range :- ")
    t1 = time.time()
    a = int(args.split("-")[0]) 
    b = int(args.split("-")[1])
    print()
    threads = []

    for x in range (a,b+1):
        t = threading.Thread(target=scan , args=(ip,x))
        t.daemon = True
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()    
    t2 = time.time()
    print()
    print(f"Scanned {b-a+1} ports in {t2-t1} seconds.")

main()
