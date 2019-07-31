'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

lower = int(input("Enter the lower bound: "))
upper = int(input("enter the upper bound: ")) + 1

result = 0

for i in range(lower, upper):
	result += i

print(result)