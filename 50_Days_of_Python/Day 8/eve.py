#Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function
#returns the difference between the largest even number in the list and the smallest odd number in the list. For example, 
#if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(lst):
    evens = [i for i in lst if i % 2 == 0]
    odds = [i for i in lst if i % 2 != 0]
    return max(evens) - min(odds)
print(odd_even([1,2,4,6])) #5