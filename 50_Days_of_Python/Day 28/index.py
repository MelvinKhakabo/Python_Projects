#Write a function called index_position. This function takes a string 
#as a parameter and returns the positions or indexes of all lower 
#letters in the string. For example ‘LovE’ should return [1,2].

def index_position(a):
    return [i for i in range(len(a)) if a[i].islower()]
print(index_position('LovE'))

  


