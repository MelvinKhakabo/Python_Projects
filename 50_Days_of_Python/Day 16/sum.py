#Write a function called sum_list with one parameter that takes a 
#nested list of integers as an argument and returns the sum of the 
#integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an 
#argument your function should return a sum of 33.

def sum_list(nested_list):
    total = 0
    for i in nested_list:
        for j in i:
            total += j
    return total    
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]])) #33
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6], [1, 2, 3, 4]])) #38
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6], [1, 2, 3, 4], [2, 3, 4, 5]])) #43