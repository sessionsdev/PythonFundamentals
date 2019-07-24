'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

sample_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
u_list = []

for i in sample_list:
    if sample_list.count(i) < 2:
            u_list.append(i)

print(u_list)
