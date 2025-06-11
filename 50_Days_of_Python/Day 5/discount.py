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
        
        discount_amount = (discount / 100) * price
        final_price = price - discount_amount
        
        return final_price
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
# Example usage
if __name__ == "__main__":
    final_price = my_discount()
    if final_price is not None:
        print(f"The price after discount is: {final_price:.2f}")
    else:
        print("Could not calculate the price after discount due to invalid input.")
        





