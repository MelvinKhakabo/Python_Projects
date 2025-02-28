#The areas variable, containing the area of different rooms in your house, is already defined.
#Write a for loop that iterates over all elements of the areas list and prints out every element separately.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

#Using indexing to access elements in a for loop:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print("index" + str(index) + ":" + str(a))

