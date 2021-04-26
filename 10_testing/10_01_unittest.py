'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
tests should pass. Also include a test that does not pass.

NOTE: You can write both the code as well as the tests for it in this single file.
However, feel free to adhere to best practices and separate your tests and the functions you are testing
into different files. Note that you will run into an error when attempting to import this file,
because Python modules can't begin with a number.

'''
import unittest
# write a function with input parameters and a return value
def sequence(first, second):
    try:
        return [first, second, second / first, (second / first) / second]
    except ZeroDivisionError:
        return 'first number can\'t be 0'

def longsequence(first, second, length):
    try:
        sequence = [first, second]
        while len(sequence) < length:
            sequence.append(sequence[-1] / sequence[-2])
        return sequence
    except ZeroDivisionError:
        return 'first number can\'t be 0'

class TestResults(unittest.TestCase):
    # test resulting sequence
    def test_result(self):
        self.assertEqual(sequence(3, 2), [3, 2, 0.6666666666666666, 0.33333333333333333])
    # test exception message
    def test_except(self):
        self.assertEqual(sequence(0, 2), 'first number can\'t be 0')
    # should not pass, exception should be handled
    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            sequence(0, 2)

if __name__ == '__main__':
  unittest.main()