#Write a function called user_name that generates a username from the user’s email. The code should ask the user to input an email and 
#the code should return everything before the @ sign as their user name. For example, if someone enters ben@gmail.com, the code 
#should return ben as their user name.


# The code should also handle the case where the user enters an invalid email address.
# For example, if someone enters ben@gmail, the code should return an error message saying that the email address is invalid.
def user_name(email):
    if "@" not in email or "." not in email.split("@")[1]:
        return "Invalid email address"
    else:
        return email.split("@")[0]

email = input("Enter your email: ")
print(user_name(email))