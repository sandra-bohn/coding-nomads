'''
Write a script that demonstrates a try/except/else.

'''
list_ = [1, 'one', -2, 23, 3, 'three', 0, '', [], 2]
for i in list_:
    try:
        print(2 / i)
    except TypeError:
        print('That\'s not a number!')
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    except Exception:
        print('I don\'t know what went wrong there!')
    else:
        print('That worked!')
