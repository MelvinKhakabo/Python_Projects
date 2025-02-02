#Write a function called same_in_reverse that takes a string and 
#checks if the string reads the same in reverse. If it is the same, the 
#code should return True if not, it should return False. For example, 
#‘dad’ should return True, because it reads the same in reverse.

def same_in_reverse(word):
    return word == word[::-1]   
print(same_in_reverse('dad')) #True
print(same_in_reverse('love')) #False
print(same_in_reverse('madam')) #True
print(same_in_reverse('hello')) #False