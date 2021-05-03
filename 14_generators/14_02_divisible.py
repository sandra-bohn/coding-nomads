'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
gen = (x for x in range(1, 10000) if x % 1111 == 0)

for i in gen:
    print(i)
