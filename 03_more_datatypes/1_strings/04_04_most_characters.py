'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")
string_3 = input("Enter third string: ")
longest = ""

if (len(string_1) > len(string_2)) and (len(string_1) > len(string_3)):
    longest = string_1
elif (len(string_2) > len(string_1)) and (len(string_2) > len(string_3)):
    longest = string_2
else:
    longest = string_3

print(".............")
print(f"The longest string is: {longest}")

# print(max(string_1, string_2, string_3))
