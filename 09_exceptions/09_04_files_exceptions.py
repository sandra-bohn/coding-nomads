'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
import os

# write a custom Exception that inherits from Exception and raise it if the
# first 100 characters of any of the files contain the string "Prince".
class PrinceError(Exception):
    pass

# Open war_and_peace.txt, read the whole file content and store it in a variable
try:
    with open('./books/war_and_peace.txt', 'r') as fin:
        war_and_peace = fin.readlines()
except FileNotFoundError:
    print('File not found, skipping War and Peace.')

# Open crime_and_punishment.txt and overwrite the whole content with an empty string
try:
    with open('./books/crime_and_punishment.txt', 'w') as fout:
        fout.write('')
except FileNotFoundError:
    print('File not found, skipping Crime and Punishment.')

# Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
try:
    for f in os.listdir('./books'):
        if f.find('copy') == -1:
            with open('./books/' + f) as fin:
                text = fin.readlines()
                try:
                    print(f'The first character in {f} is {str(text[0])[0]}')
                    if str(text[0]).find('Prince') > -1:
                        raise PrinceError
                except IndexError:
                    print(f'{f} is empty.')
                except PrinceError:
                    print(f'{f} is probably boring, it talks about princes!')
except FileNotFoundError:
    print('Books directory not found.')
