#Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function
#returns the difference between the largest even number in the list and the smallest odd number in the list. For example, 
#if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.


def odd_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    if not even_numbers or not odd_numbers:
        return None

    largest_even = max(even_numbers)
    smallest_odd = min(odd_numbers)

    return largest_even - smallest_odd
print(odd_even([1, 2, 4, 6]))  # Output: 5
print(odd_even([1, 3, 5, 7]))  # Output: None
print(odd_even([2, 4, 6, 8]))  # Output: None
print(odd_even([1, 3, 5, 7, 2]))  # Output: 5
print(odd_even([1, 2, 3, 4, 5, 6]))  # Output: 4
