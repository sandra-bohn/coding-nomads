'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
gen = (x for x in range(1, 10000) if x % 1111 == 0)

for i in gen:
    print(i // 1111)
