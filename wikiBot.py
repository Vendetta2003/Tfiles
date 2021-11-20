from bs4 import BeautifulSoup
import requests
from os import system
# need to increase efficiency

def main():
    def inp():
      global  query 
      query  = input("Enter query - ")
      system("cls")

    def parser2(some_text):
        c = 0
        f_out=""
        for ch in some_text:
            if (ch=="<" or ch==">" ):
                c+=1
            elif(c%2==0 and ord(ch)!=10):
                f_out+=ch
        
        return f_out.replace("[","").replace("]","")


    def get_data(query:str):
        response = requests.get(f"https://en.wikipedia.org/wiki/{query}")

        sp = BeautifulSoup(response.text, "html.parser")

        if("Wikipedia does not have an article with this exact name." not in str(response.text) and "Bad title" not in str(response.text)):
                d1 = sp.find(id = "firstHeading")  
                d2 = sp.find(class_="mw-parser-output")
                d3 = d2.find_all("p")[2:4]
                if(len(parser2(str(d3)))!=0):
                    print("------[+]"+parser2(str(d1))+"[+]--------")
                    print(parser2(str(d3)))
                    print("-----------------------")
                else:
                    print("[-] No valid data found :(")
        else:
            print("[-]No entry found in wikipedia.")
    inp()
    get_data(query=query)

if (__name__ == "__main__"):
    main()



