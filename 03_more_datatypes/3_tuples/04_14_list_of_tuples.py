'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

phrase = input("Enter a new sentence: ")
result_list = []

split_phrase = phrase.split()

for i in split_phrase:
    result_list.append(tuple(i))


print(result_list)