#Write a function called sort_words that takes a string of words as an 
#argument, removes the whitespaces, and returns a list of letters 
#sorted in alphabetical order. Letters will be separated by commas. All 
#letters should appear once in the list. This means that you sort and 
#remove duplicates. For example ‘love life’ should return as 
#['e,f,i,l,o,v'].

def sort_words(words):
    return sorted(set(words.replace(' ', '')))

print(sort_words('love life')) #['e', 'f', 'i', 'l', 'o', 'v']
print(sort_words('python')) #['h', 'n', 'o', 'p', 't', 'y']
print(sort_words('hello world')) #['d', 'e', 'h', 'l', 'o', 'r', 'w']
print(sort_words('hello')) #['e', 'h', 'l', 'o']