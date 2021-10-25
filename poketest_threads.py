import requests
from bs4 import BeautifulSoup
import threading
from time import time

def main():
    pokemon = input("Enter a pokemon name or its id - ")

    t1= time()
    url  = f"https://pokemondb.net/pokedex/{pokemon}"

    response = requests.get(url)


    data1 = BeautifulSoup(response.text, "html.parser")

    data2 = str(data1.find_all("table"))

    data3 = data2.split("</table>")

    datax = data3[0]

    c = 0
    p_id , p_t = "" , ""

    for ch in datax:
        if(ord(ch)==10):
            c+=1
        if(c==4):
            p_id +=ch
        if(c==9):
            p_t +=ch

    c  = 0

    f_pid  , f_pt = "" , ""

    for ch in p_id:
        if(ch=="<" or ch==">"):
            c+=1
        elif(c%2==0):
            f_pid+=ch

    c = 0

    for ch in p_t:
        if(ch=="<" or ch==">"):
            c+=1
        elif(c%2==0):
            f_pt+=ch


    fout ="Name - "+str(data1.find("h1")).replace("<h1>","").replace("</h1>","") +"\nType(s)- " +f_pt + "\nid - "+f_pid

    if(str(data1.find("h1")).replace("<h1>","").replace("</h1>","")!="Page not found"):
        print(fout)
    else:
        print("Wrong pokemon name or id")
    
    t2 = time()
    print(t2-t1)

   
threads = []


for x in range(4):
    t = threading.Thread(target=main())
    threads.append(t)
    t.daemon = True
    threads[x].start()

    
print(threads)




#for j in range(5):
    #threads[i].join()
