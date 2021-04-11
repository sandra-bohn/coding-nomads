'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
# Get number
num = int(input("Enter a number between 0 and 1,000,000,000: "))
# find number
i = 0
while i != num:
    i += 1
print(f"The number you entered was {i}.")
