#Write a function called guess_a_number. The function should ask a user to guess a randomly generated number. 
#If the user guesses a higher number, the code should tell them that the guess is too high, 
#if the user guesses low, the code should tell them that their guess is too low. 
#The user should get a maximum of three guesses. When the user guesses right, the code should declare them a winner. After 
#three wrong guesses, the code should declare them a loser.

import random

def guess_a_number():
    number = random.randint(1, 10)
    for i in range(3):
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            return "You are a winner"
        elif guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    return "You are a loser"

