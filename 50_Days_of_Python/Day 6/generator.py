#Write a function called user_name that generates a username from the user’s email. The code should ask the user to input an email and 
#the code should return everything before the @ sign as their user name. For example, if someone enters ben@gmail.com, the code 
#should return ben as their user name.

def user_name(email):
    email = str(input("Enter your email:")),
    return email.split("@")[0]
print(user_name('email')) 

