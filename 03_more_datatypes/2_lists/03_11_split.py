'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
# Get string
text = input("Enter text: ")
# Make text lowercase and take out commas and periods
text = text.lower()
text = text.replace(',', '')
text = text.replace('.', '')
# Split string into list of words
wordlist = text.split()
# Count occurrences of each word
wordset = set(wordlist)
print("The words in your passage are:", wordset)
most = 0
mostword = []
for i in wordset:
    if wordlist.count(i) > most:
        most = wordlist.count(i)
        mostword = [i]
    elif wordlist.count(i) == most:
        mostword.append(i)
print("The most common word(s) is/are", mostword)
