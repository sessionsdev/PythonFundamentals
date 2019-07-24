'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

vowels = "aeiouAEIOU"

phrase = input("Enter a phrase or sentence: ")

v_counter = 0

for i in phrase:
    for j in vowels:
        if i == j:
            v_counter += 1

print(v_counter)
            