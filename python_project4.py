alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
          's','u','v','w','x','y','z']
def encrption(text,shift):
 ciper_text=""
 for char in text: #h=9 position
        position=alphabet.index(char)#hello ppositon=7
        new_position=(position+shift)%26
        ciper_text+=alphabet[new_position]
 print(f"the text of encrption is {ciper_text}")
 def decryption(text,shift):
  plain_text=""
 for char in text: #khoor
        position=alphabet.index(char)
        new_position=(position-shift)%26
        plain_text+=alphabet[new_position]
 print(f"the text of decryption is {plain_text}")
what_to_do=input("type encrpt for encrption and decrpyt for decrption ")
text=input("enter the message ")
shift=int(input("enter the shift key "))
if what_to_do=="encrpt":
    encrption(text,shift)
elif what_to_do=="decrpyt":
 decryption(text,shift)
#if we enterjenny it will give error because we donot have key ex 
#y index is 25 and 25+3=28 then it will give error the we have make it in formula 
# %26
