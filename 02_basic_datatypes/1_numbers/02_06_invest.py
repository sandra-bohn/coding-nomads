'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
# Get user inputs
amt = float(input("How much do you want to invest? "))
rate = float(input("What is the interest rate in percentage? "))
time = int(input("How many years do you want to invest? "))
# Print balance for each year
year = 1
while year <= time:
    amt = (1 + rate / 100) * amt
    print("After", year, "year(s) your balance will be", "%.2f" % amt)
    year = year + 1
