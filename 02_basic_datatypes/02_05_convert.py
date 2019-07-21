'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 66
y = 43.62

print(float(x))  # to float

print(int(y))  # to int

print(x // y)  # floor division

var1 = int(input("Enter the first number: "))

var2 = int(input("Enter the first number: "))

print(var1 * var2)  # mulitplication with user inputs
