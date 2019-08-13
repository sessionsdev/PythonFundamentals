'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("enter the second Number: "))
    print(num1 / num2)
except: TypeError
    print("Cant divide by zero")