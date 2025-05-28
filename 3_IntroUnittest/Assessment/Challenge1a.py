###############################################################################
# Python Unittest - Assertions
###############################################################################
import unittest

class InvalidOperation(Exception): ...

def simple_calculator(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '%':
        return a % b
    if op == '//':
        return a // b
    
    raise InvalidOperation(f'{op} is not a valid operation.')


class TestChallenge1(unittest.TestCase):

    def test_operations(self):
        input_output: list[tuple[tuple[int, int, str], int]] = [
            ((1, 1, '+'),  2),
            ((1, 1, '-'),  0),
            ((1, 8, '*'),  8),
            ((8, 2, '/'),  4),
            ((5, 2, '%'),  1),
            ((5, 2, '//'), 2)
        ]
        ###############################################################################
        # 
        # Assignment:
        #
        # 
        # Ensure all existing operators defined in the simple_calculator function
        # return the expected results. 
        # 
        # The above input_output list contains the arguments to simple_calculator 
        # and the expected output.
        # 
        # Breakdown:
        # input_output[0] == ((1, 1, '+'),  2) # ((args),  output)
        # 
        # 
        # 1.) For each input/output pair in the above input_output list:
        #       a. ) Provide the arguments to the simple_calculator function and 
        #           assert that the return value equals the output.
        ###############################################################################
        # Add test code below
        for args, expected in input_output:
            result = simple_calculator(*args)
            self.assertEqual(result, expected)
        # End test code
        ###############################################################################
        


    def test_unknown_operation(self):
        input_side_effect: list[tuple[tuple[int, int, str], Exception]] = [
            ((1, 1, '&'),  InvalidOperation),
            ((1, 1, '^'),  InvalidOperation),
            ((1, 8, '@'),  InvalidOperation),
        ]
        ###############################################################################
        # 
        # Assignment:
        #
        # 
        # Ensure undefined operators raise InvalidOperation exceptions.
        #
        # 1.) For each input/side effect pair in the above input_side_effect list:
        #       a. ) Provide the arguments to the simple_calculator function and 
        #           assert that InvalidOperation is raised.
        ###############################################################################
        # Add test code below
        for args, exception in input_side_effect:
            with self.assertRaises(exception):
                simple_calculator(*args)
        # End test code
        ###############################################################################

if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))