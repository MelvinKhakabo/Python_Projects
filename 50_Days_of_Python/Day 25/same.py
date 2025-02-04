#Create a function called all_the_same that takes one argument, a 
#string, a list, or a tuple and checks if all the elements are the same. 
#If the elements are the same, the function should return True. If not,
#it should return False. For example, [‘Mary’, ‘Mary’, ‘Mary’] should 
#return True.

def all_the_same(data):
    return len(set(data)) == 1  # set() removes duplicates from the list

print(all_the_same([1, 1, 1])) #True
print(all_the_same([1, 2, 1])) #False