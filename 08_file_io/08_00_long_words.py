'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
# make empty word list
words = []

# open file in read mode
with open('words.txt', 'r') as fin:
    # import contents
    text = fin.readlines()
    # make list of words with line breaks stripped
    for i in text:
        words.append(i.rstrip())
# print words more than 20 characters long
for w in words:
    if len(w) > 20:
        print(w)
