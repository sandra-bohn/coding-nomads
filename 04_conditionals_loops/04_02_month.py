'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

# Make dictionary of months
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
          7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
# Get number from user
number = int(input("Enter a number that corresponds to a month: "))
# Print the month
if number in months:
    print(months[number])
else:
    print("Other")
# Use a nested if statement:
if number <= 12:
    if number >= 1:
        print(months[number])
else:
    print("Other")
