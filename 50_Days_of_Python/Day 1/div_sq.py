#Day 1: Divide or Square
#Write a function called divide_or_square that takes one argument (a number), 
#and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. 
#For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

def divide_or_square(num):
    """
    This function takes a number as input and returns the square root of the number if it is divisible by 5.
    Otherwise, it returns the remainder when the number is divided by 5.
    """
    if num % 5 == 0:
        return round(num ** 0.5, 2)  # Return square root rounded to 2 decimal places
    else:
        return num % 5  # Return remainder when divided by 5

print(divide_or_square(10))  # Output: 3.16 (square root of 10)
print(divide_or_square(25))  # Output: 5.0 (square root of 25)