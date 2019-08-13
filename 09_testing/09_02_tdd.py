'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
# def add numbers and double
# get two numbers from user, x, y
# add two numbers together
# multiply by 2
# return print(result)

def AddThenDouble(x, y):
    pass

import unittest

class AddThenDoubleTest(unittest.TestCase):

    def test_AddThenDouble(self):
        self.assertEquals(AddThenDouble(5, 5), 20)
        self.assertEquals(AddThenDouble(-1, 2), 2)
        self.assertEquals(AddThenDouble(2.3, 1), 3.6)
        with self.assertRaises(TypeError):
            AddThenDouble("ten", 5)

if __name__ == '__main__':
    unittest.main()


