#Write a function called repeated_name that finds the most repeated name in the following list.
#name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
def repeated_name(names):
    name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    most_repeated = max(set(name), key = name.count)
    return most_repeated
print(repeated_name('name'))  



#Extra Challenge: Sort by Last Name
#b. You work for a local school in your area. The school has a list of names of students saved in a list. 
#The school has asked you to write a program that takes a list of names and sorts them alphabetically. 
#The names should be sorted by last names. Here is a list of names:
#[‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris Brown’,’Tom Cruise’]
#Your code should not just sort them alphabetically, but it should also switch the names (the last name must be the first). Here is how your 
#code output should look:
#['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']
#Write a function called sorted_names.


def sorted_names(names):
    names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
    sorted_names = sorted(names, key=lambda name: name.split()[-1])
    switched_names = [f"{name.split()[-1]} {name.split()[0]}" for name in sorted_names]
    return switched_names
print(sorted_names('names'))

    


