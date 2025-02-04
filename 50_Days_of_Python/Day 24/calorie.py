#Create a function called average_calories that calculates the average 
#calories intake of a user. The function should ask the user to input their 
#calories intake for any number of days it should calculate and return the average intake.

def average_calories():
    days = int(input("Enter the number of days: "))
    total_calories = 0
    for day in range(1, days + 1):
        calories = int(input(f"Enter the calories for day {day}: "))
        total_calories += calories
    return total_calories / days