'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

phrase = input("Enter a sentence: ")

split_list = phrase.split()

counter = 0
word = split_list[0]

for i in split_list:
    frequency = split_list.count(i)
    if(frequency > counter):
        counter = frequency
        word = i

print(word)