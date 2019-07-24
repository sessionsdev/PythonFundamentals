'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''



sentence = input("Please enter a sentence:")
symbol = input("Please enter a symbol: ")

first_letter = sentence[0]

new_sentence = sentence.replace(first_letter, symbol)

print(new_sentence)