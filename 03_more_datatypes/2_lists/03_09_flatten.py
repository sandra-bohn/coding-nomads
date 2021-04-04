'''
Write a script that "flattens" a shallow list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note that your input list only contains one level of nested lists.
This is called a "shallow list".

CHALLENGE: Do some research online and find a solution that works
to flatten a list of any depth. Can you understand the code used?

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# For loop way
flattened_list = []
for i in starting_list:
    if type(i) is list:
        for j in i:
            flattened_list.append(j)
    else:
        flattened_list.append(i)

print(flattened_list)

# Sum way
flat_list = sum(starting_list, [])
print(flat_list)

