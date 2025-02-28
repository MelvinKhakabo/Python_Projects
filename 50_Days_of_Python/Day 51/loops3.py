#iterating though dictionaries and numpy arrays
#dictionaries req methods, and numpy arrays req functions(nditer). In Python3 you need items method to iterate through a dictionary.

#Iterating over a dictionary(unordered)
#Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for x, y in europe.items():
    print("the capital of " + x  + " is " + str(y))



#Loop over Numpy array
#1d numpy array is similar to a list(for x in my_array :  ...) 
#A 2d numpy array is similar to a list of lists.
#for x in np.nditer(my_array) : ...

# Import numpy as np
import numpy as np

# For loop over np_height( 1D array)
#inches = "inches"
#for height in np_height:  
#    print(f"{height} {inches}")  

# For loop over np_baseball (2D array)
#for x in np.nditer(np_baseball):
#    print(x)