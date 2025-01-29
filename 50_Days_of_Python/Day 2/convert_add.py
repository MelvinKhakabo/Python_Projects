#Day 2:Strings to Integers
#Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. For example 
# [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed 
 
def convert_add(list):
    return sum([int(i) for i in list])

list = ['1', '3', '5']
print(convert_add(list))