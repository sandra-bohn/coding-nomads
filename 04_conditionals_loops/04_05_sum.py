'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
# Get numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
# Calculate sum
sum = 0
for i in range(num1, num2 + 1):
    sum += i
print(f"The sum is: {sum}")
