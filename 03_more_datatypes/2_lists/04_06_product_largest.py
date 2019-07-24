'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
numbers = []


for i in range(10):
    num = int(input("Please enter a number: "))
    numbers.append(num)

numbers.sort()

highest = numbers[(len(numbers) -1)]

print(f"The highest number you entered is: {highest}")

#challenge

product = 1

for i in range((len(numbers)-1)):
    product = product * numbers[i]

print(f"The product of the numbers entered is: {product}")
