#Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the 
#string. For example ‘hello’ should return:{‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


