# Void function
def printSadness():
    print("Sadness!")
    print("Sadness!")
    print("Sadness!")

# Void function with arguments (x being the argument in this case)
def printXtimes3(x):
    print(str(x))
    print(str(x))
    print(str(x))

# Return function
def getStateOfLife():
    return "Ultimate dispair!!"

# Example of return function with arguments
def add(a, b):
    return a + b

result = add(6, 2)

# Funtion call (Executing the mentioned function)
printSadness()
printXtimes3("Extreme sadness!") # the value within the brackets is telling what x (the argument) should be
print(getStateOfLife())          # a return function is giving information from the function to the function call
print(str(add(6, 2)))            # the arguments (6 and 2) are getting slotted into the a and be spots in the argument