'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# Get sentence
sentence = input("Enter a sentence: ")
# Get symbol
symbol = input("Enter a symbol: ")
# Make replacement ignore case
sentence = sentence.lower()
# Get first letter of sentence
first = sentence[0]
# Print result
print(sentence.replace(first, symbol))
