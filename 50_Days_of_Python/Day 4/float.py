#Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, returns 1 if only 
#one argument is a float, and returns 0 if neither argument is a float.
#If you pass (12.1, 23) as an argument, your function should return a 1.

def only_floats(a, b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0
a = 12.1
b = 23
print(only_floats(a, b)) #1