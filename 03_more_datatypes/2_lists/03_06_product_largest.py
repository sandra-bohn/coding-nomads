'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# Get numbers
numbers = input("Enter a list of 10 numbers separated by spaces: ")
numlist = numbers.split()
# Make list floats
floats = []
for i in numlist:
    floats.append(float(i))
# Print largest number
print("The largest number you entered was", max(floats))
# Print product of numbers
product = 1
for i in floats:
    product *= i
print("The product of the numbers you entered was", product)
