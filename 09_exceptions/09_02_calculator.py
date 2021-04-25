'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    # get input and check that it's a number
    try:
        dividend = float(input('Enter a number: '))
    except ValueError:
        print('You didn\'t enter a number. Try again.')
        continue
    try:
        divisor = float(input('Enter another number: '))
    except ValueError:
        print('You didn\'t enter a number. Try again.')
        continue
    # calculate the quotient
    try:
        print(f'{dividend} / {divisor} = {dividend/divisor}')
    except ZeroDivisionError:
        print('You cannot divide by 0. Try again.')