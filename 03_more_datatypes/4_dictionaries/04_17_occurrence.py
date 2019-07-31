'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

my_string = input("Enter a string: ")
my_dict = dict()

for i in my_string:
    my_dict[i] = my_string.count(i)

print(my_dict)
    