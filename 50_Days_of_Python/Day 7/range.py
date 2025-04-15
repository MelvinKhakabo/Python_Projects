#Write a function called string_range that takes a single number and returns a string of its range. The string characters should be 
#separated by dots(.) For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.


def string_range(n):
    """
    Returns a string of numbers from 0 to n-1, separated by dots.
    
    Parameters:
    n (int): The upper limit of the range.
    
    Returns:
    str: A string of numbers from 0 to n-1, separated by dots.
    """
    return '.'.join(str(i) for i in range(n))

