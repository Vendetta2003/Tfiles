import threading
import os 
import sys
# usage  - python netscanner0.py <Number of hosts to scan in the current network>
# it uses 192.168.0.1-255 as its ip range. 

def main():
    def ping(ip):
        resp = str(os.popen(f"ping -n 1 {ip}").read())
        if ("Destination host unreachable" not in resp):
            print(f"[+] Host is up - {ip}")
        else:
            print(f"[-] Host is down - {ip}")
        
    threads  = []
    a = int(sys.argv[1])
    a = a+1
    
    for x in range(a):
        t = threading.Thread(target=ping , args=(f"192.168.0.{x}",))
        threads.append(t)
    try:
        for x in range(a):
            threads[x].start()

        for x in range(a):
            threads[x].join()

    except Exception as e :
        print(e)
        pass

if __name__ == "__main__":
    main()