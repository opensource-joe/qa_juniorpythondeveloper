###############################################################################
# Python Unittest - Mocking
###############################################################################
import json
import unittest
from unittest.mock import MagicMock
from urllib.request import urlopen


def get_json(url, getter_callable=urlopen):
    with getter_callable(url) as f:
        return json.loads(f.read())


class TestChallenge2(unittest.TestCase):

    def test_get_json(self):
        expect = {
            "sun": 80,
            "mon": 86,
            "tue": 92,
            "wed": 76,
            "thu": 79,
            "fri": 91,
            "sat": 87
        }
        test_url = 'http://cloudacademy.com/weather'
        ###############################################################################
        # 
        # Assignment:
        #
        # 
        # Ensure the get_json function returns a Python dictionary containing the results of
        # the above expect dictionary. 
        #
        # 1.) Mock the urlopen context manager such that calling the read method returns
        #       a json string matching: json.dumps(expect)
        #
        # 2.) Call the get_json function.
        #   - Provide the test_url and the mocked urlopen as arguments.
        #
        # 3.) Assert that the results from get_json match expect.
        #
        # 4.) Assert that the mocked urlopen was called with the test_url
        ###############################################################################
        # Add test code below
        
        # End test code
        ###############################################################################
        

if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))
