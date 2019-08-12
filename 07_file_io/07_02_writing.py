'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

file = "/home/jonathan/Documents/CodingNomads/Labs/python_fundamentals/07_file_io/words.txt"

with open(file, encoding='utf-8') as contents:
    contents = contents.read()
    contents = contents.split()

    reversed_contents = str(contents[::-1])


f = open("words_reversed.txt", "w+")
f.write(reversed_contents)
f.close()

