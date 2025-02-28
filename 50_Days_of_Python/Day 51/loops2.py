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
for index, area in enumerate(areas):
    print("room" + str(index) + ":" + str(area))



#Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))



#Loop over list of lists
#Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

#nested loop# Build a for loop from scratch
for room in house:
    print(room)
    for item in room:
        print(item)