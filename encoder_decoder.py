# Python Lab 6
# Author: Ashley Maurer
#test 3
#test 2:58
if __name__ == "__main__":
    option = -1
    while option != 3:
        print("Menu  \n------------- \n1. Encode  \n2. Decode  \n3. Quit \n")
        option = int(input("Please enter an option: "))
        if option == 1:
            orig_pass = input("Please enter your password to encode: ")
            encoded_pass = [int(i) + 3 for i in orig_pass]
            print("Your password has been encoded and stored!\n")
