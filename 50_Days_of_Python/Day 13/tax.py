#Write a function called your_vat. The function takes no parameter. 
#The function asks the user to input the price of an item and VAT 
#(vat should be a percentage). The function should return the price 
#of the item plus VAT. If the price is 220 and, VAT is 15% your code 
#should return a vat inclusive price of 253. Make sure that your code 
#can handle ValueError. Ensure the code runs until valid numbers 
#are entered. (hint: Your code should include a while loop).

def your_vat():
    price = float(input('Enter the price: '))
    vat = float(input('Enter the VAT: '))
    return price + (price * (vat / 100))

print(your_vat())
# Output:
# Enter the price: 220  
# Enter the VAT: 15 
# 253.0