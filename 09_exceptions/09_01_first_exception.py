'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

try:
    list_ = ["hello world!"]
    print(list_[1])
except IndexError:
    print('You only have one item in your list so you cannot print the second item.')
