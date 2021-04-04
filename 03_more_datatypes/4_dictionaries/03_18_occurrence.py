'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
# Get string
user_input = input("Enter text: ")
# Create list and set of letters
wordlist = user_input.split()
letterlist = []
for i in wordlist:
    letterlist.append(list(i))
letterlist = sum(letterlist, [])
letterset = set(letterlist)
# Make dictionary
result = {}
for j in letterset:
    result[j] = letterlist.count(j)
# Print result
print(result)
