# Introduction to Patching

## Introduction
The [unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#patch), opens in a new tab callable is used to replace objects for a limited scope. The patch callable can be used as a context manager or callable decorator. Patches remain in effect for the life of the context manager or decorated callable.

Patches are commonly used during testing to replace external resources with alternate implementations.

Patches replace objects with [MagicMock](https://docs.python.org/3/library/unittest.mock.html#magic-mock), opens in a new tab by default. [AsyncMock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock), opens in a new tab is used when decorating async callables. Patches can specify an object or callable as the replacement object.

``` python
from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# Patch can be used as a context manager. 
# The first argument is a target object to replace. 
# The target is a str representing the package.module.object
with patch(f'builtins.print') as print_mock:
    # The builtin print callable will be replaced inside this code block.
    greeter('World')
    # Inspect the mock version of the print callable and determine if it
    # was provided with the expected input.
    print_mock.assert_called_with('Hello, World')
    print_mock.assert_called_once()
# Outside the context manager print behaves normally.
greeter('World')
###############################################################################
print('No assertion errors')
```

---

## New
By default patch uses ```MagicMock``` as the replacement object. The new keyword argument of the patch callable specifies an alternate replacement object.

``` python
from unittest.mock import patch
def user_choice(prompt):
    return input(prompt)
with patch(f'builtins.input', new=lambda _prompt: 3):
    '''
        The keyword argument 'new' replaces the target with an object. 
        In this example the object is a lambda function.
        The lambda function is a shorthand for the following:
        >>> def fake_input(_prompt):
        ...    return 3 
        The unused _prompt parameter is included for context.
    '''
    # The builtin input callable will be replaced inside this code block.
    # The lambda function used to replace input is hardcoded to return 3.
    assert user_choice('select a number between 1 and 10') == 3
###############################################################################
print('No assertion errors')
```

---

## Using New_Callable
The **new_callable** keyword argument of the ```patch``` callable specifies a callable to replace the default ```unittest.mock.MagicMock``` callable. The ```patch``` callable calls the **new_callable** and uses the return value as the replacement object.

``` python
from io import StringIO
from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# StringIO is an in-memory text stream that can replace standard output for testing.
# https://docs.python.org/3.9/library/io.html#io.StringIO
with patch(f'sys.stdout', new_callable=StringIO) as stdout_mock:
    ''' The keyword argument 'new_callable' replaces the default callable: unittest.mock.MagicMock. '''
    greeter('World')
    # stdout_mock is a StringIO object containing the text that was passed to print by the greeter function.
    assert stdout_mock.getvalue() == 'Hello, World\n' # \n is an end of line character.
###############################################################################
print('No assertion errors')
```

---

## Using: Spec and Auto-Spec
```Mock``` objects create attributes and methods on-demand giving them the ability to replace other objects. Allowing for maximum flexibility, mocks don't enforce restrictions on allowed attributes or callable parameters. These allowed differences can lead to tests which are tightly coupled to mock objects rather than the objects being mocked.

The ```unittest.mock``` module includes a mechanism called spec which is used to ensure mock objects adhere more closely to the object being mocked.

The **spec** keyword argument of the patch callable passes the argument through to the spec argument of the default mock callable.

Spec is useful for ensuring that mocks include the same attributes and methods as the provided object. However, spec allows callables to be called with any arguments without considering the defined parameters of the callable. The auto-spec feature enforces call signatures.

``` python
from unittest.mock import patch
class KeepingItClassy:
    def add(self, a, b):
        return self.a + self.b
if __name__ == '__main__':
    # Spec
    with patch(f'__main__.KeepingItClassy', spec=KeepingItClassy) as keep_it_classy_mock:
        ''' The keyword argument 'spec' passes the argument to unittest.mock.MagicMock. '''
        keep_it_classy_mock.add.return_value = 2
        assert keep_it_classy_mock.add(1, 1) == 2
        keep_it_classy_mock.add.assert_called_with(1, 1)
        keep_it_classy_mock.add.assert_called_once()
        try:
            # Attempt to access a non-existent attribute.
            keep_it_classy_mock.non_existent_attr
        except AttributeError:
            print(
                'Spec matches the attributes of the patched object.\n'
                'Non-existent attributes raise an AttributeError exception when accessed.'
            )
        # spec doesn't enforce method signatures.
        # Calling add would result in a TypeError if this was the real KeepingItClassy
        assert keep_it_classy_mock.add() == 2
        keep_it_classy_mock.add.assert_called_with()
    # Auto-spec
    with patch(f'__main__.KeepingItClassy', autospec=True) as keep_it_classy_mock:
        ''' The keyword argument 'autospec' conforms to the structure of the mocked object. '''
        keep_it_classy_mock.add.return_value = 2
        assert keep_it_classy_mock.add(1, 1) == 2
        keep_it_classy_mock.add.assert_called_with(1, 1)
        keep_it_classy_mock.add.assert_called_once()
        try:
            # Attempt to access a non-existent attribute.
            keep_it_classy_mock.non_existent_attr
        except AttributeError:
            print(
                'Auto-spec matches the attributes of the patched object.\n'
                'Non-existent attributes raise an AttributeError exception when accessed.'
            )
        try:
            keep_it_classy_mock.add()
        except TypeError:
            print('Auto-spec enforces method signatures.')
###############################################################################
print('No assertion errors')
```

---

## Function Decorators
The ```patch``` callable can be used as a callable decorator. The patch remains in effect for the duration of the patched callable. Decorators pass replacement objects as arguments to decorated callables.

``` python
from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# Replace the built-in print function with a Mock for this function only.
@patch(f'builtins.print')
def test_greeter(print_mock):
    # The patch decorator passes mocked objects as input parameters.
    #
    # With the print function replaced with a mock for the duration of 
    # this method no data is printed to the console.
    greeter('World')
    # Inspect the mock version of the print function and determine if it
    # was provided with the expected input.
    print_mock.assert_called_with('Hello, World')
    print_mock.assert_called_once()
test_greeter()
###############################################################################
print('No assertion errors')
```

---

## Multiple Decorators
Patch decorators are stackable. The Python runtime runs decorators from bottom to top. The callable signature matches the bottom up order of the decorators.

``` python
from unittest.mock import patch
def greeter():
    name = input("What's your name? ")
    print(f'Hello, {name}')
@patch(f'builtins.print')
@patch(f'builtins.input')
def test_stacks(input_mock, print_mock):
    # The patch decorators pass mocked objects as input parameters.
    # Python runs decorators from the bottom up.
    # The order of the input parameters match.
    input_mock.return_value = 'World'
    # Running greeter will call input and print.
    greeter()
    # Verify the calls
    input_mock.assert_called_once()
    print_mock.assert_called_with('Hello, World')
test_stacks()
###############################################################################
print('No assertion errors')
```

---

## Patching Test Cases
The ```patch``` callable is commonly used during testing. Patch can decorate all or individual methods by applying the decorator to classes or methods.

``` python
import unittest
from unittest.mock import call, patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
def greet_everyone(*names):
    ''' A function used to demonstrate the use of the patch callable. '''
    for name in names:
        print(f'Hello, {name}')
############################## Patching Methods ###############################
#
class GreeterTest(unittest.TestCase):
    # Replace the built-in print function with a Mock for this method only.
    @patch(f'builtins.print')
    def test_greeter(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        # 
        # With the print function replaced with a mock for the duration of 
        # this method no data is printed to the console.
        greeter('World')
        # Inspect the mock version of the print function and determine if it
        # was provided with the expected input.
        print_mock.assert_called_with('Hello, World')
        print_mock.assert_called_once()
############################## Patching Classes ###############################
#
# Replace the built-in print function for all methods of this class.
@patch(f'builtins.print')
class GreetEveryoneTest(unittest.TestCase):
    def test_greeter(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        greeter('World')
        # Inspect the mock version of the print function and determine if it
        # was provided with the expected input.
        print_mock.assert_called_with('Hello, World')
        print_mock.assert_called_once()
    def test_greet_everyone(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        greet_everyone('World', 'Universe', 'Multiverse', 'Ultraverse')
        # The expected calls made to the mock implementation of print.
        expect = [
            call('Hello, World'), 
            call('Hello, Universe'), 
            call('Hello, Multiverse'), 
            call('Hello, Ultraverse'), 
        ]
        # Ensure the calls made to print are passed the expected arguments.
        assert print_mock.mock_calls == expect
        assert print_mock.call_count == len(expect)
###############################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
```

---

## Specific Patches
Specific types of patches exist for select use cases. Patch includes callables for [patching dictionaries](https://docs.python.org/3/library/unittest.mock.html#patch-dict), opens in a new tab, [class attributes and methods](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object), opens in a new tab, and [multiple attributes](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple), opens in a new tab. These specific patch callables can be used as context managers and decorators.

``` python
import unittest
from unittest.mock import call, patch
##################### Patching Class Attributes & Methods #####################
class KeepingItClassy:
    class_attribute = print
    @classmethod
    def class_method(cls, *args):
        ...
# Patch class: attributes & methods
with patch.object(KeepingItClassy, 'class_method') as class_method_mock:
    # The class method has been replaced by a magic mock.
    KeepingItClassy.class_method(1, 2, 3)
    class_method_mock.assert_called_with(1, 2, 3)
with patch.object(KeepingItClassy, 'class_attribute') as class_attr_mock:
    # The class attribute has been replaced by a magic mock.
    KeepingItClassy.class_attribute('hello')
    class_attr_mock.assert_called_with('hello')
############################ Patching Dictionaries ############################
# Dictionary containing fake configuration data.
config = { 'hostname': 'prod.server.addr', 'port': 5001 }
# patch.dict can replace values in a dictionary for the scope of the patch.
with patch.dict(config, {'hostname': 'test.server.addr'}) as config_mock:
    assert config['hostname'] == 'test.server.addr'
    # This value remains unchanged.
    assert config['port'] == 5001
######################## Patching Multiple Attributes #########################
from unittest.mock import DEFAULT
import sqlite3
hostname = 'prod.server.addr'
database = sqlite3
if __name__ == '__main__':
    with patch.multiple('__main__', hostname=':memory:', database=DEFAULT) as replacements:
        # patch.multiple returns a dictionary. 
        # Keys match the names of the patched attributes.
        database_mock = replacements['database']
        # Host name is replaced with a new str for the scope of this patch.
        assert hostname == ':memory:'
        # DEFAULT creates a mock using the default mock type.
        database_mock.connect(hostname)
        # Confirm that connect was called.
        database_mock.connect.assert_called_with(hostname)
###############################################################################
print('No assertion errors')
```

---

## Summary
The [unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#patch), callable is used to replace objects during a limited scope. The patch callable can be used as a context manager or callable decorator.

Patches are commonly used during testing to replace external resources with alternate implementations. Allowing code to be tested independently of its dependencies.

Patch defaults to MagicMock as the replacement object. Async callables default to AsyncMock as the replacement object. The patch callable includes keyword arguments for specifying alternate replacement objects.

Specific types of patches exist for use cases such as patching a dict, class, or multiple attributes.

The patch callable replaces an object bound to a name with an alternate object for a limited scope. Patches must be applied to objects where they're looked up rather than where they're defined. The official Python 3 documentation includes a detailed explanation found [here](https://docs.python.org/3/library/unittest.mock.html#where-to-patch).