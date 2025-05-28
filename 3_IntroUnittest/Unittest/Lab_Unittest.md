# Lab Notes

## Introduction ot Unittest
The [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest), opens in a new tab is Python's built-in testing module. Used to create and run unit and integration tests.

**All software contains developer assumptions.**

Erroneous assumptions can result in software defects of varying degrees of severity. Unittest enables developers to test software assumptions using Python code. Unittest is designed around the notion of performing an **action** and making an **assertion** regarding the results. Actions are events which produce or change: objects and or external resources.

Actions are taken and assertions are made about the state of the results. Assertions raise an exception when results don't match what's expected. Indicating that a codified assumption is no longer accurate.

The following code represents a basic unittest example. This example tests Python's built-in int callable. Tests are defined as methods of a unittest.TestCase, opens in a new tab class. Test cases represent concepts which can be tested as a single entity. For example: objects, functions, and methods. Test methods can contain zero or more assertions. A test passes when all assertions inside the test method are successful.

``` python
import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope') 
if __name__ == '__main__':
    unittest.main()
```

## Test Runner: Main
The unittest module includes a mechanism for running tests called a test runner. The test runner is used to run one or more tests from one or more test cases.

``` python
import unittest 
...
# Q: What does __name__ == '__main__' do?
# A: It determines if this code is being run directly.
# Example: $ python3 code_file.py
# It doesn't run if this code file is imported as a module.
if __name__ == '__main__':
    unittest.main()
```

Actual code test. Above is explaining '__main__'.
``` python
import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope') 
if __name__ == '__main__':
    # Increase the verbosity of the console output and stop all tests after the first - if any -- assertion fails
    # Similar to using the CLI flags: python3 test_assertion.py -v -f
    unittest.main(verbosity=2, failfast=True)
```

Configuration can be specific with command line flags. "-h" for help.
``` python
python3 cloudacademy/test_assertion.py -h 
```

## Test Runner: CLI
The test runner can be started by invoking the unittest module as a command line application. Including options to run one or more test modules, test cases, or test methods.

``` python
import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope')
```

Starts the runner as a CLI call.
```
python3 -m unittest cloudacademy.test_assertion.TestExample -v -f
```

## Test Runner: Discovery
The unittest module includes a test discovery mechanism, opens in a new tab mechanism based on filename patterns. Allowing multiple test cases inside a module to be run together.

[Unittest module's production test suite](https://github.com/python/cpython/blob/main/Lib/unittest/main.py)

Display files to be discovered and run.
``` python
ls -lash /usr/local/lib/python3.11/unittest/test
```

Discover and run tests in the IDEs terminal pane.
``` python
python3 -m unittest discover /usr/local/lib/python3.11/unittest/test "test*.py"
```

## Test Cases
The unittest module takes an object-oriented approach to testing; introducing a base class used as a test building block called a **test case**.

Test cases define a context for performing tests. Any concept which can be treated as a single unit can be a test case. Including: functions, class definitions, workflows, etc.

A class becomes a test case by inheriting from [unittest.TestCase](https://docs.python.org/3.9/library/unittest.html#unittest.TestCase), opens in a new tab.

Class definitions for test cases often include the name Test at the start or end of the class name.

Tests are defined by creating methods with names starting with the word test. This naming convention is used by the test runner to identify tests. When the test runner encounters test* methods it recognizes and runs them.

``` python
import unittest
class TestMethods(unittest.TestCase):
    def test_should_run(self):
        self.assertTrue(True)
    def wont_run(self):
        self.assertTrue(False)
if __name__ == '__main__':
    unittest.main()
```

```
python3 cloudacademy/test_assertion.py -v -f
```

## Test Cases: Assertions
The [unittest.TestCase](https://docs.python.org/3.9/library/unittest.html#unittest.TestCase), opens in a new tab base class defines methods for performing assertions. These methods are used to compare and inspect objects in different ways.

Tests use one or more assertion methods to test assumptions.
``` python
import unittest
class Test(unittest.TestCase):
    def test_common_assertion_methods(self):
        ''' A non-exhaustive demonstration of many of the common methods
            The unittest.TestCase class provides methods for different types of assertions. 
        '''
        # Compare any two objects using the assertEqual method.
        # A method version of the == operator.
        self.assertEqual('hey', 'hey')
        # With a message
        # All assert* methods allow a message to be provided.
        # The message is displayed in the test runner if the assertion is false.
        # The message argument is omitted in the remaining examples for brevity.
        self.assertEqual(1, 1, 'there has been a disturbance in the force.')
        # Compare any two objects using the assertNotEqual method.
        # A method version of the != operator.
        self.assertNotEqual('hey', 'sup')
        # Check the `truthiness` of an object using assertTrue.
        self.assertTrue('hey' == 'hey')
        # Check the `truthiness` of an object using assertFalse.
        self.assertFalse('hey' == 'sup')
        # Check the identity of an object using assertIs.
        # A method version of the `is` operator.
        greeting_a = 'hey'
        greeting_b = greeting_a
        # Do both name bindings reference the same object in memory?
        # Yes. Same str
        self.assertIs(greeting_a, greeting_b)
        # Check the identity of an object using assertIsNot.
        greeting_a = 'hey'
        greeting_b = 'sup'
        # Do both name bindings reference the same object in memory?
        # No, since they're two different strs.
        self.assertIsNot(greeting_a, greeting_b)
        # Check if an expression evaluates to None using the assertIsNone.
        # Hardcoded None
        self.assertIsNone(None)
        # Expression
        self.assertIsNone(1 == 2 or None)
        # Since 1 does not equal 2 None is returned.
        # Check if an expression evaluates to something other than None using the assertIsNotNone.
        self.assertIsNotNone(1 == 2)
        # Check if an object exists inside a collection using the assertIn.
        self.assertIn(3, [1,2,3,4,5,6])
        # Check if an object does not exist inside a collection using the assertNotIn.
        self.assertNotIn(7, [1,2,3,4,5,6])
        # Check if an object is a specific instance of a class using the assertIsInstance.
        self.assertIsInstance('hey', str)
        self.assertIsInstance(12345, int)
        # Example with a user defined class:
        class Hey: ...
        self.assertIsInstance(Hey(), Hey)
        # Check if an object is not a specific instance of a class using the assertNotIsInstance.
        self.assertNotIsInstance('hey', int)
        self.assertNotIsInstance(12345, str)
        # Example with a user defined class:
        class Hey: ...
        self.assertNotIsInstance(Hey(), str)
        # Check if a callable raises a specific exception using the assertRaises.
        # This assert is a bit different from the others in that a callable is passed as an argument.
        # `int` is the callable that will be run. 
        # Arguments to the right of the callable are passed to the callable.
        # This is similar to:
        # int('not a number')
        # Which raises a ValueError
        self.assertRaises(ValueError, int, 'not a number')
if __name__ == '__main__':
    unittest.main()
```

```
python3 cloudacademy/test_assertion.py
```

## Test Cases: Setup/Teardown
Test cases may consist of many test methods. To reduce repeated code the ```TestCase``` base class includes setup and teardown methods. These methods are run before each test allowing tests to use shared resources.

This is commonly used to set up connections to external services such as databases.

``` python
import unittest
import sqlite3
class TestSetupTeardown(unittest.TestCase):
    def setUp(self):
        ''' Actions to take before running each test. '''
        # Create a connection to a SQLite database.
        # This instance is an in-memory only instance.
        # 
        # Each time a connection is created the database will be empty.
        self.db_connection = sqlite3.connect(':memory:')
        # 
        curs = self.db_connection.cursor()
        # Create a database table named greeting with a single text column called name.
        curs.execute("CREATE TABLE greeting (name text);")
        # Commit to the changes.
        self.db_connection.commit()
    def tearDown(self):
        ''' Actions to take after running each test. '''
        # Close the connection to the database.
        # Which may be superfluous for an in-memory database.
        self.db_connection.close()
    def test_row_insert(self):
        expect = 'Hello'
        # setUp runs before this method and binds the database connection to the db_connection attribute.
        curs = self.db_connection.cursor()
        # Insert the word 'Hello' into the name column of the greeting table.
        curs.execute("INSERT INTO greeting VALUES (?);", (expect,))
        # Commit to the changes.
        self.db_connection.commit()
        # Fetch the newly inserted row and extract the first (and only) column.
        actual = curs.execute("SELECT name FROM greeting;").fetchone()[0]
        # Assert that the greeting returned is the same as the greeting written to the DB.
        self.assertTrue(expect == actual)
    def test_starts_empty(self):
        # setUp runs before this method and binds the database connection to the db_connection attribute.
        curs = self.db_connection.cursor()
        # The fetchone method will return None if no data is returned from the DB.
        self.assertIsNone(curs.execute("SELECT name FROM greeting;").fetchone())
if __name__ == '__main__':
    unittest.main()
```

```
python3 cloudacademy/test_assertion.py
```

## Test Cases: Skip Tests
Test methods can be conditionally skipped using decorator functions or ```TestCase``` methods. This is useful in scenarios where tests aren't required for a given operating system, Python version, module version, etc.

``` python
import unittest
import sys
class TestSkipIt(unittest.TestCase):
    @unittest.skip('always skipped')
    def test_skip(self):
        self.fail('will not run because test is skipped.')
    # Skip a test unless a condition is met.
    @unittest.skipIf(sys.version_info.major >= 3, 'Python 2 only.')
    def test_skip_if(self):
        self.fail('will not run because test is skipped.')
    # Skip a test unless a condition is met.
    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows only test.')
    def test_skip_unless(self):
        self.fail('will not run because test is skipped.')
    # Conditionally skip a test method from inside the test.
    def test_possibly_skip(self):
        if True:
            self.skipTest('skip based on some condition')
        # If not skipped then perform some test.
        self.assertTrue(True)
    # This test will run.
    def test_is_number(self):
        # Ensure that str objects which represent ints are correctly converted to int.
        self.assertTrue(int('10') == 10)
        # Ensure that other valid int representations produce ints.
        # For example int literals allow underscores for added readability.
        self.assertTrue(int('1_000') == 1_000)
        # Numbers represented in base 2 (binary) are ints too. 
        # Change the base number system to 2 and check
        self.assertTrue(int('011', base=2) == 3)
if __name__ == '__main__':
    unittest.main()
```

```
python3 cloudacademy/test_assertion.py
```

## Test Failures
Incorrect assertions result in failing test methods. Failed tests display the traceback in the console.

``` python
import unittest
class TestFailures(unittest.TestCase):
    def test_failures(self):
        self.assertTrue(False, 'oh no!')
if __name__ == '__main__':
    unittest.main()
```

```
python3 cloudacademy/test_assertion.py
```

## Summary
Python's built-in [unittest module](https://docs.python.org/3.8/library/unittest.html), opens in a new tab is a testing framework for creating unit and integration tests.

Tests are created inside of test cases. Test cases are created by subclassing the unittest.TestCase class. TestCase includes methods for performing setup and teardown, making assertions, among others.

Tests are defined by methods which start with the word test. Tests are located and run by the test runner.

The test runner can be started using the unittest.main callable. Unittest.main can be configured with keyword arguments and or command line flags. The test runner can also be started by invoking the unittest module on the command line.

The unittest module is worth knowing because it's built into Python's standard library. Which makes it accessible without adding third-party dependencies.

### Keep Learning
TODO: Complete these labs.
- [Introduction to Mocking](https://platform.qa.com/lab/python-unittest-mock/)
- [Introduction to Patching](https://platform.qa.com/lab/python-unittest-patch/)

Point of Interest: The unittest module was based on a popular Java testing framework called jUnit. Unittest ignores many of Python's idioms in favor of mirroring jUnit, which followed Java's idioms. There are third-party Pythonic testing libraries such as [Pytest](https://docs.pytest.org/en/7.1.x/contents.html). Pytest uses Python's assert keyword to make assertions rather than specific assertion methods. It also locates tests based on naming conventions which removes the need to subclass unittest.TestCase.