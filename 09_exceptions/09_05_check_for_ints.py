'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
integer = None
while integer is None:
    try:
        integer = int(input('Enter an integer: '))
    except ValueError:
        print('That\'s not an integer, try again.')
    else:
        print('That was an integer!')
