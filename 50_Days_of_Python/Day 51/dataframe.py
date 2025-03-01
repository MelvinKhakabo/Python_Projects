#looping over a Dataframe
#import pandas as pd
# Import cars data
#import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
#for lab, row in cars.iterrows():
#    print({lab})
#    print(row)

#use iterators lab and row, to adopt the code to print out the row label and the cars per capita
# Iterate over rows of cars
# Import cars data
#import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
#for lab, row in cars.iterrows() :
#    print(lab + ": " + str(row['cars_per_cap']))


#add column called country to cars dataframe# Import cars data
# Import cars data
#import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
#for lab, row in cars.iterrows():
    # Check what you're assigning to the COUNTRY column
#    print(row["country"].upper())  #uppercase country name
#    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
#print(cars)