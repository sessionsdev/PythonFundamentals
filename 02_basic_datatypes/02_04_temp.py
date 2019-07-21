'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temp = float(input("Enter the tempature in fahrenheit: "))

f_to_c = (temp - 32) * (5 / 9)

print(f"{round(temp, 2)} degrees fahrenheit = {round(f_to_c, 2)} degrees celsius")
