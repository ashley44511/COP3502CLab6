#Author: Ashley Maurer
def decode(password):
    #decodes encoded password by subtracting 3 to each digit in password
    return [int(i) - 3 for i in password]