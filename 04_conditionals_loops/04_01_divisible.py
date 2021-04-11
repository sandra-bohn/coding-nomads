'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

# Get number
number = float(input("Enter a number between 1 and 1,000,000,000: "))
if number > 1000000000:
    print("Your number is too large.")
elif number < 1:
    print("Your number is too small.")
elif number % 3 == 0:
    print(f"Your number is divisible by 3, the answer is {int(number / 3)}.")
else:
    print("Your number is not divisible by 3.")