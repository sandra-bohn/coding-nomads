'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(object, start = 0):
    enumerator = []
    index = 0
    for i in object:
        enumerator += [(start + index, i)]
        index += 1
    return enumerator

mylist = ['one', 'two', 'three', 'four']
print(list(my_enumerate(mylist, 1)))
