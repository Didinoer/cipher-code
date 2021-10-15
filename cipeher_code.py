a=1
while a > 0 :
    action = input("input 'encode' for encrypt the code or 'decode' for deccrypy the code : input 'n' for exit \n")
    if action == "n" :
        print("you terminate this program. thank you ")
        break
    text = input("masukan code :\n").lower()
    shift = int(input("masukan berapa longkapnya : "))

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def encode(textp,shiftp) :
        encoded_text =""
        for i in textp :
            text_position_start = alphabet.index(i) 
            a = text_position_start + int(shiftp)
            b = alphabet[a]
            encoded_text += b
        print(f"sucsessfully encoded : {encoded_text}")
        
    def decode (texto,shifto) :
        decoded_text =""
        for i in texto :
            text_position_start = alphabet.index(i)
            a = text_position_start -(shifto)
            b = alphabet[a]
            decoded_text += b
        print(f"sucsessfully encoded : {decoded_text}")

            

    if action == 'encode' :
        encode(text,shift)
    elif action == 'decode' :
        decode(text,shift)
    

   



    
      