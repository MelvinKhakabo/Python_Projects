#Write a function called check_pangram that takes a string and checks if it is a pangram. 
#A pangram is a sentence that contains all the letters of the alphabet. If it is a pangram, 
#the function should return True, otherwise, return False. 
# The following sentence is a pangram so it should return True:
#'the quick brown fox jumps over a lazy dog

def check_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in string:
            return False
    return True
