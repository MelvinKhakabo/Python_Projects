#Write a function called check_pangram that takes a string and checks if it is a pangram. 
#A pangram is a sentence that contains all the letters of the alphabet. If it is a pangram, 
#the function should return True, otherwise, return False. 
# The following sentence is a pangram so it should return True:
#'the quick brown fox jumps over a lazy dog

sentence = "the quick brown fox jumps over the lazy dog"
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
print(is_pangram(sentence)) #True