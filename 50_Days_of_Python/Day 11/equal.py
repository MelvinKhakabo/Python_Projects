#Write a function called equal_strings. This takes two strings 
#as arguments and compares them. If the strings are equal (if they 
#have the same characters and have equal length), it should return 
#True, if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

def equal_strings(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False
print(equal_strings("Love", "Evol")) #True

