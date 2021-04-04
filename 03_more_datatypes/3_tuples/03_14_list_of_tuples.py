'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# Get string
input_string = input("Enter a phrase: ")
# Create list of words
wordlist = input_string.split()
# Create list of tuples
result_list = []
for i in wordlist:
    result_list.append(tuple(list(i)))
print(result_list)
