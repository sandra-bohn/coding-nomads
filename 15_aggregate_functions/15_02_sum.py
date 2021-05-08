'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(list_):
    ans = 0
    for i in list_:
        ans += i
    return ans

print(sum([1, 2, 3, 4, 5]))
