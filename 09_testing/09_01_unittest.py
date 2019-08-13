'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

def subtract_divide(dividend, x, y):
    try:
        
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        return f"this won't work, {x} - {y} is 0 or lower."

import unittest

class SubtractDivideTest(unittest.TestCase):
    
    def test_subtract_divide(self):

        self.assertEquals(subtract_divide(10, 100, 90), 1)
        self.assertEquals(subtract_divide(250, 100, 50), 5)
        self.assertEquals(subtract_divide(20, 10, 5), 6)


if __name__ == '__main__':
    unittest.main()
