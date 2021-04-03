'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
# Get phrase
phrase = input("Enter a phrase: ")
# Get letter
letter = input("Enter a letter in your phrase: ")
# Print index of first occurrence of letter
print("The index of the first occurrence of your letter is", phrase.index(letter))
