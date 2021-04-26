'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import unittest
# replace f with fart
class TestFart(unittest.TestCase):
    # test resulting string
    def test_resultf(self):
        self.assertEqual(ftofart('forty'), 'fartorty')
    def test_resultF(self):
        self.assertEqual(ftofart('Forty'), 'Fartorty')
    # test handling of non-string input
    def test_error(self):
        with self.assertRaises(AttributeError):
            ftofart(40)

# make all numbers negative
class TestNegative(unittest.TestCase):
    # test that negative stays negative
    def test_resultneg(self):
        self.assertEqual(makenegative(-10), -10)
    # test that positive becomes negative
    def test_resultpos(self):
        self.assertEqual(makenegative(10), -10)
    # test that 0 stays 0
    def test_result0(self):
        self.assertEqual(makenegative(0), 0)
    # handle TypeError for non-numeric input
    def test_error(self):
        with self.assertRaises(TypeError):
            makenegative('ten')

if __name__ == '__main__':
  unittest.main()