#Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word. For example, 
#‘i like learning’ becomes ‘I Like Learning’.

def capitalize(string):
    return string.title()
print(capitalize('i like learning')) #I Like Learning
print(capitalize('i like learning python')) #I Like Learning Python
print(capitalize('i like learning python and javascript')) #I Like Learning Python And Javascript