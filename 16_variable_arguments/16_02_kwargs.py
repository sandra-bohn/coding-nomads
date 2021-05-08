'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def describe_me(**descriptors):
    for k, v in descriptors.items():
        print(f"My {k} is {v}.")

describe_me(name='Sandra', age=39)
