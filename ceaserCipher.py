logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(message,shift):
    new_message = ""
    for index in message:
        position = alphabet.index(index)
        new_position = position + shift
        new_message += alphabet[new_position]
    print(f"Your encrypted message : {new_message}")

def decrypt(message,shift):
    new_message = ""
    for index in message:
        position = alphabet.index(index)
        newPostion = position - shift
        new_message += alphabet[newPostion]
    print(f"Your message : {new_message}")

def ceaser(message,shift,direction):
    if direction == "encode":
        encrypt(message=message,shift=shift)
    elif direction == "decode":
        decrypt(message=message,shift=shift)

print(logo)
user_ = input("Enter 'encode' to encrypt the message, and 'decode' decrypt the message : ")
if user_ == "encode" or user_ == "decode":
    message = input("Type your message here : ").lower()
    shift = int(input("Enter number of spaces to shift : "))
    if shift < ( 26 - len(message) ) :
        if user_ == "encode":
            ceaser(message=message,shift=shift,direction="encode")
        else:
            ceaser(message=message,shift=shift,direction="decode")
    else:
        print("Enter a valid shifting.")
else:
    print("Enter valid operation.")
