'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
# make empty word list
words = []

# open file in read mode
with open('words.txt', 'r') as fin:
    # import contents
    text = fin.readlines()
    # make list of words with line breaks stripped
    for i in text:
        words.append(i)

# write words in reverse
with open('words_reverse.txt', 'w') as fout:
    for w in range(1, len(words) + 1):
        fout.write(words[w * -1])
