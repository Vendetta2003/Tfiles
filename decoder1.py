def decode_username(data:str):#{'_id': '881621205013110805', 'username': 'pokemon123'}
    c = 0
    decoded_data = ""
    for i in range(len(data)):
        ch = data[i]
        if(ch=="'"):
            c = c+1
        if (c>=5 and c<=7):
            decoded_data = decoded_data + ch
    decoded_data = decoded_data.replace("'","")
    return decoded_data

#print(decode_username("{'_id': '881621205013110805', 'username': 'pokemon123'}"))
# used this in dicord bot for guild, so that it can have a database of members. This method is the parser.
