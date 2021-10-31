import pyshark
from hex_decoder import decode , layer2
import time 
import pyautogui

print("Quick change the screen to main window")
time.sleep(3)# 3 second counter 
x , y = 600 , 643#coordinates of chatbox (max screen)

capture = pyshark.LiveCapture(interface="Ethernet 2",display_filter="tcp")
send =""
state = 1 #0 to deactivate 1 to activate


for packet in capture.sniff_continuously():
   if (int(packet.tcp.len)>15 and packet.ip.src=="198.251.89.115"  and "000" not in layer2(decode(packet.tcp.payload)) and int(packet.tcp.len)<100 ):
            print(layer2(decode(packet.tcp.payload)),send)
            print("--------------------------------------")
            if(layer2(decode(packet.tcp.payload))!=send and state == 1):
                pyautogui.click(x,y)
                pyautogui.write(send)
                time.sleep(.1)
                pyautogui.press("enter")
                send = layer2(decode(packet.tcp.payload))

            