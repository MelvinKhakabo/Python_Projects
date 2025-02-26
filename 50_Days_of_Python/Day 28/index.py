#Write a function called index_position. This function takes a string 
#as a parameter and returns the positions or indexes of all lower 
#letters in the string. For example ‘LovE’ should return [1,2].

def index_position(string):
    return [i for i in range(len(string)) if string[i].islower()]
print(index_position('LovE')) #[1, 2]

