'''
Write a script with a function that demonstrates the use of *args.

'''

def sum(*numbers):
    ans = 0
    for i in numbers:
        ans += i
    return ans

print(sum(1, 2, 3, 4, 5))
