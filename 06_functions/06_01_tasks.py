'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divisible_or(n):
    """Returns TRUE if parameter is divisible by 4 or 7"""
    answer = (n % 4 == 0 or n % 7 == 0)
    return answer

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divisible_and(n):
    """Returns TRUE if parameter is divisible by 4 and 7"""
    answer = (n % 4 == 0 and n % 7 == 0)
    return answer
# take in a number from the user between 1 and 1,000,000,000
user_input = int(input("Enter a number between 1 and 1,000,000,000: "))
# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
result_or = divisible_or(user_input)
result_and = divisible_and(user_input)
# print your new variables to display the results
print("Divisible by 4 or 7: ", result_or)
print("Divisible by 4 and 7: ", result_and)
