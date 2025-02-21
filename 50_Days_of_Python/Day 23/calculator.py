#Create a simple calculator. The calculator should be able to perform basic math operations, add, subtract, divide and multiply. The calculator 
#should take input from users. The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'You cannot divide by zero'

def operate(operator, num1, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return 'Invalid operator'   

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")   
num2 = float(input("Enter the second number: "))

result = operate(operator, num1, num2)
