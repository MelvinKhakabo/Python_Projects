#Create a function called generate_password that generates any length of password for the user. 
#The password should have arandom mix of upper letters, lower letters, numbers, and punctuation symbols. 
#The function should ask the user how strong they want the password to be. 
#The user should pick from -weak, strong, and very strong. 
# If the user picks weak, the function should generate a 5 character long password. 
#If the user picks strong, generate an 8 character password and if they pick very strong, generate a 12 character password.

import random
import string

def generate_password(length, strength):
    password = ''
    if strength == 'weak':
        length = 5
    elif strength == 'strong':
        length = 8
    elif strength == 'very strong':
        length = 12
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password
