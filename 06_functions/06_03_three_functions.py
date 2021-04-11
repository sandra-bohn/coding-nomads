'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
# This program outputs a user's possible NPR names,
# which adds the user's middle initial to their first name
# and uses a small foreign town they visited as their last name.

import random

# Get user's first name and middle initial
firstname = input("What is your first name? ")
initial = input("What is your middle initial? ")
# Get foreign towns user has visited
town = input("Enter small foreign towns you've visited, separated by spaces: ")
towns = town.split()

# Function to produce possible first NPR names
def newname(oldname: str, middleinitial: str):
    # Adds middle initial to first name to generate list of first names
    newnames = [middleinitial + oldname]
    for spot in range(0, len(oldname)):
        letterlist = list(oldname)
        tempname = ''
        for letter in range(0, spot):
            tempname += letterlist[letter]
        tempname += middleinitial
        for letter2 in range(spot, len(letterlist)):
            tempname += letterlist[letter2]
        newnames += [tempname]
    newnames += [oldname + middleinitial]
    return newnames

# Function to produce possible pairs of names
def makepair(first, mi, last):
    # Pairs random new firstname with random last name
    firstnames = newname(first, mi)
    namepair = random.choice(firstnames).capitalize() + ' ' + random.choice(last)
    return namepair

# Function to ask user to approve choice
def approve(option):
    # Presents an option to a user and asks for approval
    answer = input(f"Does {option} work? (y or n) ")
    return answer

# Present options to user
chosen = 'n'
while chosen != 'y':
    chosen = approve(makepair(firstname, initial, towns))
