'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def add_html_tag(tag):
    def decorator_func(input_func):
        def wrapper_func(*args):
            print(tag)
            value = input_func(*args)
            print(tag)
            return value
        return wrapper_func
    return decorator_func

@add_html_tag('<p>')
def fix_case(*args):
    for i in args:
        print(i.capitalize())
    return args

fix_case('hello')
