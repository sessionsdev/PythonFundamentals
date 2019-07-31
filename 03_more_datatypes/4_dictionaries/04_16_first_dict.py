'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

# Method 1

my_dict = dict()

for x in range(1, 11):
    my_dict[x] = x*x

print(my_dict)



# method 2

my_dict2 = {x: x*x for x in range(1, 11)}

print(my_dict2)
