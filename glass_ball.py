# Imagine you have several glass balls and are in an n-story building. If you throw the balls below a certain floor, they will not break. 
# If you are above or at that certain floor, they will break. Write a function to find the floor where the balls begin breaking -- in the minimum possible amount of attempts/throws.
# You will not see the floor input, but it will be a part of a pre-existing function that you will call at each throw 
# (ie. you can call the function with the current floor and get True if the ball breaks, False if not).

# This function will return True if the floor passed in will break the ball, 
# false if not. do not touch any of the functionality - you will code in the next function
# You can change the threshold argument to another number if you 
# want to test different cases
def floorCheck(floor, threshold = 42):
	return floor >= threshold

def findBreakFloor(n):
    pass


print(floorCheck(51))