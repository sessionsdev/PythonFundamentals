'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
phrase = input("Enter a phrase or sentence: ")

letter = input("Enter the letter you want to find: ")

print(phrase.find(letter))