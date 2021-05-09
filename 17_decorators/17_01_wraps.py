"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""
def add_paragraph(input_func):
    def wrapper_func(*args):
        print('<p>')
        value = input_func(*args)
        print('<p>')
        return value
    return wrapper_func

@add_paragraph
def fix_case(*args):
    for i in args:
        print(i.capitalize())
    return args

fix_case('hello')
