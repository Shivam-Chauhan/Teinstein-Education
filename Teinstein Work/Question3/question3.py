import socket
from collections import defaultdict
from cryptography.fernet import Fernet


def encryption(password_inp,key):    # This function is used to encrypt data
    message = password_inp.encode()  # Every Key is unique
    function = Fernet(key)
    encrypt = function.encrypt(message)
    return encrypt
    # Returning the encrypted data


def decryption(password_inp,key):  # This function is used to decrpyt the data
    f = Fernet(key)                # Key will remains same
    decrypted = f.decrypt(password_inp)
    return decrypted.decode()


if __name__== '__main__':
    database=defaultdict(list)   # This is a datastructure used to store username-->[encrypted data, key]
    all_keys=set()               # set to check if the key exist or not O(log(n)) operation
    ct=1
    
    choice=int(input("Press 1 for Encryption or 2 for Decryption :- "))
    if choice==1:           # Choice 1
        while True:   
            if ct==5:                # This will automatically reject the user after five attempts
                break
            email=input("Please enter email or phone_number :- ")
            if email in database.keys():  
                print("User already Exist")
            else:
                content=input("Please enter the content you want to encrypt :-")
                key=Fernet.generate_key()
                while key in all_keys:     # Checking if the generated key is present in the table or not if yes than change it.
                    key=Fernet.generate_key()
                all_keys.add(key)
                data=encryption(content,key)
                database[email]=[data,key]  # Storing the key->value pair  O(1) operation
                print("Your encrypted data:- ")
                print(data)
                break
            ct+=1

    elif choice==2:         # Choice 2
        while True:   
            if ct==5:                # This will automatically reject the user after five attempts
                break
            user_name=input("Enter User Name :- ")
            if user_name not in database:
                print("Invalid")
            else:
                data=decryption(database[user_name][0],database[user_name][1])  # Decrypting the data
                print("Decrpted Data:- ")
                print(data)
                break
            ct+=1
    else:
        print("Oops!! you have pressed the wrong key.")

    ct+=1
    
    
# Here Fernet Hashing is every key is generated by it's seed.