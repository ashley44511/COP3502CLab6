# Python Lab 6
# Author: Ashley Maurer
#
if __name__ == "__main__":
    option = -1
    while option != 3:
        print("Menu  \n------------- \n1. Encode  \n2. Decode  \n3. Quit \n")
        option = int(input("Please enter an option: "))
        if option == 1: #Author: Ashley Maurer
            #encodes password
            orig_pass = input("Please enter your password to encode: ")
            encoded_pass = [int(i) + 3 for i in orig_pass]
            print("Your password has been encoded and stored!\n")
        elif option == 2: #Author: Ashley Maurer
            #decodes password (added later)
            decoded_pass = [int(i) - 3 for i in encoded_pass]
            print("The encoded password is ", end= " ")
            for i in encoded_pass: 
                print(f"{i}", end="")
            print(", and the original password is", end=" ")
            for i in decoded_pass: 
                print(f"{i}", end="")
            print(".\n")