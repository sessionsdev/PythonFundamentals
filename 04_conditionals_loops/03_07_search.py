'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

user_num = int(input("Enter a number between 1 and 1,000,000,000: "))

counter = 0

while counter < user_num:
    counter += 1

print(counter)