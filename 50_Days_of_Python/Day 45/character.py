#Write a function called analyse_string that returns the number of special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words, and, total 
#characters (all letters and special characters minus whitespaces) in a string. 
#Return everything in a dictionary format:{“special character”: “number”, “words”: “number”, “total characters”: “number”}
#Use the string below as an argument:“Python has a string format operator %. This functions analogously to 
#printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".
#Source Wikipedia.

def analyse_string(string):
    special_characters = 0
    words = 0
    total_characters = 0
    for char in string:
        if char.isalnum() == False:
            special_characters += 1
        if char == ' ':
            words += 1
        total_characters += 1
    return {"special characters": special_characters, "words": words + 1, "total characters": total_characters - words}

print(analyse_string("Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'."))