#Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the 
#string. For example ‘hello’ should return:{‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(string):
    return {i: string.count(i) for i in string}
print(count('hello')) #{'h': 1, 'e': 1, 'l': 2, 'o': 1}