#We're going to code a while loop that implements a very basic control system for an inverted pendulum. If there's an offset from standing perfectly straight, the while loop will incrementally fix the offset until the pendulum is standing straight..
#Note that if your while loop takes too long to run, or your session is expiring, you might have created an infinite loop. In particular, remember to indent the contents of the loop using four spaces or auto-indentation, and make sure the conditions are such that the loop has a stopping point.

#Create the variable offset with an initial value of 8.
#Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
#Print out the sentence "correcting...".
#Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
#Finally, still within your loop, print out offset so you can see how it changes

offset = 8
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)