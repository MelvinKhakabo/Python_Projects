#Write a function called equal_strings. The function takes two 
#as arguments and compares them. If the strings are equal (if they 
#have the same characters and have equal length), it should return 
#True, if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1, str2):
    return str1 == str2
print(equal_strings('love', 'evol')) #True