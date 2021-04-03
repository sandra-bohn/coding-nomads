'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
# Get strings
first = input("Enter a word: ")
second = input("Enter another word: ")
third = input("Enter a third word: ")
# Print output
print(len(first), first)
print(len(second), second)
print(len(third), third)
# Print only the string with the most characters
if len(first) > len(second) and len(first) > len(third):
    print(first, "has the most characters")
elif len(second) > len(first) and len(second) > len(third):
    print(second, "has the most characters")
elif len(third) > len(first) and len(third) > len(second):
    print(third, "has the most characters")
else:
    print("More than one string has the most characters")

