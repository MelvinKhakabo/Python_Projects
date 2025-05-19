#Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount
#(percentage) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function 
#should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should 
#return 127.5.


def my_discount():
    price = float(input("Enter the price: "))
    discount = float(input("Enter the discount percentage: "))
    price_after_discount = price - (price * discount / 100)
    return price_after_discount
print(my_discount()) #127.5

