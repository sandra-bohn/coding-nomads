'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


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

# find shortest and longest words
# find word lengths
lengths = []
for w in words:
    lengths.append(len(w))
minlen = min(lengths)
maxlen = max(lengths)
# add shortest and longest words to list
shortest = []
longest = []
for w in words:
    if len(w) == minlen:
        shortest.append(w)
    elif len(w) == maxlen:
        longest.append(w)

# print the results
print(f"The shortest word(s): {', '.join(shortest)}")
print(f"The longest word(s): {', '.join(longest)}")
print(f"There are {len(words)} words in the file.")
