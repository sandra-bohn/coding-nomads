'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
try:
    with open(file_name, 'r') as fin:
        try:
            number = int(fin.readline())
        except ValueError:
            print(f'The first line of {file_name} did not contain an integer. Check your file.')
        else:
            print(f'The first number in {file_name} was {number}. {number} * {number} is {number * number}.')
except IOError:
    print(f'{file_name} not found. Check your path.')
