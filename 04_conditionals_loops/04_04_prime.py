'''
Print out every prime number between 1 and 100.

'''

for number in range(2, 101):
    count = 0
    for divisor in range(2, number):
        if number % divisor == 0:
            count += 1
    if count == 0:
        print(number)
