# Python Lab 6
# Author: Ashley Maurer
#
import decode

def encode(password): #Author: Maurer
    #encodes password by adding 3 to each digit in password
    return [int(i) + 3 for i in password]

if __name__ == "__main__": #Author: Ashley Maurer
    option = -1
    while option != 3:
        print("Menu  \n------------- \n1. Encode  \n2. Decode  \n3. Quit \n")
        option = int(input("Please enter an option: "))
        if option == 1: #Author: Ashley Maurer
            #encodes password
            orig_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(orig_pass)
            print("Your password has been encoded and stored!\n")
        elif option == 2: #Author: Ashley Maurer
            #decodes password (decode function to be added later)
            decoded_pass = decode.decode(encoded_pass)
            print("The encoded password is ", end="")
            for i in encoded_pass: 
                print(f"{i}", end="")
            print(", and the original password is ", end="")
            for i in decoded_pass: 
                print(f"{i}", end="")
            print(".\n")