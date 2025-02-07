#Write a function called spelling_checker. 
#This code asks the user to input a word and if a user inputs a wrong spelling it should 
#suggest the correct spelling by asking the user if they meant to type that word. 
#If the user says no, it should ask the user to enter the word again.
#If the user says yes, it should return the correct word.
#If the word entered by the user is correctly spelled the function should return the correct word. Use the module textblob.

from textblob import Word

def spelling_checker(word):
    w = Word(word)
    if w.spellcheck()[0][0] == word:
        return word
    else:
        suggestion = w.spellcheck()[0][0]
        answer = input(f"Did you mean {suggestion}? Enter yes or no: ")
        if answer == 'yes':
            return suggestion
        else:
            return spelling_checker(input("Enter the word again: "))

word = input("Enter a word: ")
print(spelling_checker(word))