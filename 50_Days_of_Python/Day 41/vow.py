#Create a function called words_with_vowels, this function takes a 
# string of words and returns a list of only words that have vowels in them. 
# For example ‘ You have no rhythm’ should return [‘You’,’have’, ‘no’].

def words_with_vowels(a):
    vowels = 'aeiou'
    return [word for word in a.split() if any(vowel in word for vowel in vowels)]   
print(words_with_vowels('You have no rhythm')) #['You', 'have', 'no']