import requests
from bs4 import BeautifulSoup

def main():



    pokemon  = input("Enter name of pokemon - ")
    pokemon  = pokemon.strip()
    if(len(pokemon)!=0):
        pokemon = pokemon.lower()

        response  = requests.get(f'https://pokemondb.net/pokedex/{pokemon}')


        main_data = BeautifulSoup(response.text , "html.parser")




        try:
            raw_Data = str(main_data.find_all('table'))


            raw_Data2 = raw_Data.split("</table>")



            stats = raw_Data2[3]



            final_dat = ""
            c = 0

            for ch in stats:
                if(ch=="<" or ch==">"):
                    c+=1
                elif(c%2==0):
                    final_dat+=ch


            wrd = "" 
            f_out = ""

            for ch in final_dat:
                if(ord(ch)!=10):
                    wrd += ch
                else:
                    f_out = f_out+wrd+" "
                    wrd= "" 



            f_out2 =f_out.split("   ")

            print(f"Stats for - {pokemon.upper()}")

            for x in range(len(f_out2)):
                if(x%2==1):
                    if(x!=13):
                        print(f_out2[x])
                    else:
                        print(f_out2[x].replace("Min Max",""))

        except  Exception as e :
            
            print(f"No pokemon named {pokemon.upper()} found , did you mean any of the following - ")
            c2 = 0
            rawn = str(main_data.find_all('li'))
            rawn =  rawn.split(",")
            matches = ""
            wrd= ""


            for  x in rawn:
                for ch in x:
                    if(ch=="<" or ch==">"):
                        c2+=1
                    elif(c2%2==0):
                        wrd+=ch
                matches = matches+"\n"+wrd
                wrd=""
            
            print(matches)
    else:
        print("Pokemon name cant be None")

if __name__ == "__main__":
    while 1:
        main()

    
