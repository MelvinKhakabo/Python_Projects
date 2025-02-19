#Write a function called translate that takes the following words and translates them into pig Latin.
#a = 'i love python'
#Here are the rules:
#1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the end. 
#For example ‘eat’ will become ‘eatyay’
#2. If a word starts with anything other than a vowel, move the 
#first letter to the end and add ‘ay’ to the end. For example ‘day’ will become ‘ayday’.
#Your code should return:iyay ovelay ythonpay

def translate(a):
    b = a.split(' ')
    for i in range(len(b)):
        if b[i][0] in 'aeiou':
            b[i] = b[i] + 'yay'
        else:
            b[i] = b[i][1:] + b[i][0] + 'ay'
    return ' '.join(b)
