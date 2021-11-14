import socket
import threading
import time 
from threading import *



def main():
    def scan(ip , port):# 192.168.0.1 , 23-56
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        resp = s.connect_ex((ip , port))
        if(resp == 0):
              print(f"[+] Port {port} is up")
        
          
    ip = input("Enter IP addr :- ")
    args = input("Enter PORT endpoint :- ")
    t1 = time.time()
    end = int(args) 

    threads = []

    for x in range (end+1):
        t = threading.Thread(target=scan , args=(ip,x))
        t.daemon = True
        threads.append(t)
    for x in range (end+1):
        threads[x].start()
    for x in range (end+1):
        threads[x].join()    
    t2 = time.time()
    print()
    print(f"Scanned {end} ports in {t2-t1} seconds.")

main()
