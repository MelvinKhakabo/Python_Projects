#Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount
#(percentage) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function 
#should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should 


#return 127.5.



def my_discount():
    try:
        price = float(input("Enter the price of the product: "))
        discount = float(input("Enter the discount percentage: "))
        
        if price < 0 or discount < 0:
            raise ValueError("Price and discount must be non-negative.")
        
        discounted_price = price * (1 - discount / 100)
        return discounted_price
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
    print("The price after discount is:", my_discount())


