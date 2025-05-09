#Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function
#returns the difference between the largest even number in the list and the smallest odd number in the list. For example, 
#if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(numbers):
    """
    This function takes a list of numbers and returns the difference between the largest even number
    and the smallest odd number in the list.
    
    :param numbers: List of integers
    :return: Difference between largest even and smallest odd number
    """
    # Filter out even and odd numbers from the list
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    
    # Check if there are any even or odd numbers in the list
    if not evens or not odds:
        return None
    
    # Find the largest even number and smallest odd number
    largest_even = max(evens)
    smallest_odd = min(odds)
    
    # Return the difference
    return largest_even - smallest_odd
print(odd_even([1, 2, 4, 6]))  # Output: 5




