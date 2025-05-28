# Introduction to Mocking

## Introduction to Mock
The [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) module is Python's built-in mocking and patching module. Used to replace objects with fake implementations during testing.

[Mock](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.Mock) objects -- or mocks -- can replace objects with fake implementations and make assertions about how mock objects are used.

Mocks are commonly used to replace objects and external resources such as files, databases, and web APIs.

Replacing functionality with mock implementations allows code to be tested independently of its dependencies.

Key Features of Mocks:
- Mocks are callable
    - Non-callable variants exist:
        - [NonCallableMock](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.NonCallableMock)
        - [NonCallableMagicMock](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.NonCallableMagicMock)
- Mocks create attributes and methods when first accessed.
- Mocks record all calls along with arguments.
- Mocks include assertion methods used to ensure calls are made as expected.
    - Failed assertions raise an AssertionError

``` python
from unittest.mock import Mock

def greeter(name: str, display_callable: callable = print):
    ''' Demo function used to demonstrate how to use a mock in place of another object.'''
    display_callable(f'Hello, {name}')

# This will display Hello, World in the console because the built-in print
# function is the default argument for the display_callable parameter.
greeter('World')
# Call again passing a mock as the display_callable.
display = Mock()
# This will not display in the console because the mock is called in 
# place of the print function.
greeter('World', display)
# Mocks include different assertion methods used to determine if the 
# mock implementation is called as expected.
# Verify that the mock implementation of print is called with the expected
# argument value.
display.assert_called_with('Hello, World')

###############################################################################
print('No assertion errors')
```

---

## Callables
Mock objects are callable allowing them to replace callable objects with a fake implementation. Mocks accept any number of arguments and can return a value when called.

``` python
import random
from unittest.mock import Mock

################################## Callables ##################################
fake_object = Mock()

# Mocks can be called with any arguments.
fake_object('a', 'b', z=True)
fake_object(1, 2)
fake_object()

# Mocks dynamically create attributes and methods when accessed.
fake_object.fake_method()
fake_object.fake_method(1, 2, 3, 4)
fake_object.fake_method(z=True, x=False)

fake_object.fake_attribute.fake_method()
################################ Return Values ################################
#
# Mock objects can return predefined values.
#
## Keyword Argument
# 
# The return_value argument specifies the value to return when the mock is called. 
calc_pi = Mock(return_value=3.14159)

# Calls will now return the specified value.
assert calc_pi() == 3.14159

## Attribute
#
# The return_value attribute can be set after the mock is created.
calc_pi = Mock()

calc_pi.return_value = 3.14159

# Calls will now return the specified value.
assert calc_pi() == 3.14159

## Method Return Values
#
mock = Mock()

# The return_value attribute can be set on the mock method.
mock.fake_attribute.fake_method.return_value = 'method to the madness'

# Calls will now return the specified value.
assert mock.fake_attribute.fake_method() == 'method to the madness'
###############################################################################
print('No assertion errors')
```

---

## Call Assertions
Mocks record calls and provide different mechanisms for inspecting how calls were made.

Mock objects include methods used to make assertions about calls. [Assertion methods](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.Mock.assert_called) raise an [AssertionError](https://docs.python.org/3.8/library/exceptions.html#AttributeError) for False assertions. The below code demonstrates some common assertion methods.

```python
from unittest.mock import Mock

fake_object = Mock()

# The assert_not_called method ensures the mock was not called.
fake_object.assert_not_called()

# Call the mock object so that it can record the call.
fake_object('hi', 'there')

# The assert_called method ensures the mock was called at least once.
fake_object.assert_called()

# The assert_called_once method ensures the mock was called only once.
fake_object.assert_called_once()

# The assert_called_with method inspects the arguments passed to the mock the last time it was called. 
fake_object.assert_called_with('hi', 'there')

# The assert_called_once_with method ensures the mock was called only once with the specified arguments.
fake_object.assert_called_once_with('hi', 'there')

# The reset_mock method clears recorded calls allowing the mock to be reused.
fake_object.reset_mock()
fake_object.assert_not_called()

###############################################################################
print('No assertion errors')
```

---

## Inspecting Calls
Mock records all calls made along with arguments. Assertion methods can make claims about how calls are made. However, they're unable to provide detailed insights into calls.

Mocks include attributes used to access more detailed call information.

The unittest.mock module includes a helper object named [call](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.call) as a means of creating calls for comparison against recorded calls. Providing **call** the same arguments provided to a **mock call** makes the two calls comparable.

```python
from unittest.mock import call, Mock
############################### Inspecting Calls ##############################
#
fake_object = Mock()
#
# Call with positional and keyword arguments.
fake_object('hi', 'there', who='world')
# Call without arguments.
fake_object()
# The call_count attribute reflects the number of calls made to the mock.
assert fake_object.call_count == 2
# Inspecting calls more closely is done with the unittest.mock.call object.
# Call makes it easier to make assertions regarding how the mock was called.
#  
# Comparisons can be made by providing the same arguments to call that were
# provided to the mock.
#
# The calls to fake_object produce the following list of calls.
expected_calls = [call('hi', 'there', who='world'), call()]
# The assert_has_calls ensures that calls made to mock match what's expected.
# By default the order of the calls must match the order they were called.
fake_object.assert_has_calls(expected_calls)
# The any_order keyword argument ignores the call order.
fake_object.assert_has_calls(expected_calls, any_order=True)
# The call_args_list attribute stores the calls made to the mock in the
# order they were called.
assert fake_object.call_args_list == expected_calls
# Call the mock again so that this is the last call made.
fake_object('a', 'z', lang='en', case='lower')
# The call_args attribute stores the arguments of the last call as a tuple.
# The first element contains positional arguments.
# The second element contains keyword arguments.
assert fake_object.call_args == (('a', 'z'), { 'lang': 'en', 'case': 'lower' })
# Specific elements are accessible by name.
assert fake_object.call_args.args == ('a', 'z')
assert fake_object.call_args.kwargs == { 'lang': 'en', 'case': 'lower' }
# Mock doesn't record method calls in the call_args_list attribute.
# Calling a mock method.
fake_object.fake_attribute.fake_method("a")
# The method_calls attribute displays only method calls and not calls
# made directly to the mock object.
assert fake_object.method_calls == [call.fake_attribute.fake_method("a")]
# The mock_calls attribute displays all calls.
assert fake_object.mock_calls == [
    call("hi", "there", who="world"),
    call(),
    call("a", "z", lang="en", case="lower"),
    call.fake_attribute.fake_method("a"),
]
###############################################################################
print('No assertion errors')
```

---

## Magic Mock
Mock objects don't implement [magic methods](https://docs.python.org/3/reference/datamodel.html#basic-customization) by default. Magic methods are special methods used to allow objects to leverage different language features.

```python
from unittest.mock import call, MagicMock, Mock
mock = Mock()
# Invoke a magic method by passing the mock object to the int callable.
# int will check the provided object for a method named __int__
try:
    # Because mock doesn't implement magic methods this code will fail.
    # The following call produces:
    # TypeError: int() argument must be a string, a bytes-like object or a number, not 'Mock'
    int(mock)
except TypeError:
    print('Mock objects do not implement magic methods by default.')
# MagicMock is Mock with the addition of some default values for many magic methods.
mock = MagicMock()
# MagicMock returns a default int of 1
assert int(mock) == 1
# Assertions can be made against magic methods.
mock.__int__.assert_called_once()
# Values can be changed by setting the return_value of a specific magic method.
mock.__int__.return_value = 5_000
assert int(mock) == 5_000
# MagicMock returns a default length of 0
assert len(mock) == 0
mock.__len__.return_value = 10
assert len(mock) == 10
# MagicMock returns a default float of 1.0
assert float(mock) == 1.0
mock.__float__.return_value = 3.14
assert float(mock) == 3.14
# MagicMock returns a default bool of True
assert bool(mock)
mock.__bool__.return_value = False
assert not bool(mock)
# MagicMock returns a default value of False when searching a sequence
assert ':)' not in mock
mock.__contains__.return_value = True
assert ':)' in mock
# MagicMock returns an empty list by default
assert list(mock) == []
mock.__iter__.return_value = ['a', 'b', 'c']
assert list(mock) == ['a', 'b', 'c']
# Calling MagicMock objects is mostly the same as Mock.
# With an exception for calls made to magic methods.
# MagicMock tracks calls made to magic methods independently.
# Reset the mock to start with zero calls.
mock.reset_mock()
# Call the mock.__int__ method via the built-in int callable.
# Call 1.)
int(mock)
# The method_calls property stores calls to methods and attributes, and their methods and attributes.
# Calls to magic methods don't appear in the method_calls attribute.
assert mock.method_calls == []
# The mock_calls attribute tracks calls to:
# - A mock object
# - A mock object's methods
# - A mock object's magic methods
assert mock.mock_calls == [call.__int__()]
# Call 2.)
mock.fake_method('a')
# Call 3.)
mock('b')
# method_calls contains only the method call from: Call 2.
assert mock.method_calls == [call.fake_method('a')]
# mock_calls contains all three calls.
assert mock.mock_calls == [call.__int__(), call.fake_method('a'), call('b')]
###############################################################################
print('No assertion errors')
```

---

## Side Effects
Mocks return values directly by setting a mock's return_value attribute. Mock objects include another mechanism which allows for more complex call behaviors referred to as side effects. Side effects are able to raise exceptions, return multiple values, and call callables.

Side effects can be set when creating a mock using the side_effect keyword argument. They can also be set after creation using the side_effect attribute.

```python
from unittest.mock import Mock
################################### Repeated Calls ############################
# Repeated calls can return different values by specifying a list as the side_effect argument.
# The return order matches the order of the objects in the list.
mock = Mock(side_effect=['a', 'b', 'c'])
# Each call returns the next object in the list.
assert mock() == 'a'
assert mock() == 'b'
assert mock() == 'c'
# A StopIteration exception is raised when no values remain.
try:
    mock()
except StopIteration:
    print('Calling mock after all objects have been returned results in an error.')
##################################### Exceptions ##############################
# Calls can raise exceptions by specifying an exception as the side_effect argument.
mock = Mock(side_effect=Exception('Side effects can raise exceptions.'))
try:
    mock()
except Exception as ex:
    print(ex)
################################ Exceptions in Lists ##########################
# Exceptions inside a list are raised when encountered.
mock = Mock(side_effect=['a', 'b', Exception('Exceptions inside a list are raised when encountered.'), 'c'])
# The first two values...
assert mock() == 'a'
assert mock() == 'b'
try:
    # The third call encounters the exception and raises it.
    mock()
except Exception as ex:
    print(ex)
# Because the exception was handled the next call returns the next value.
assert mock() == 'c'
##################################### Functions ###############################
def multiplier(a, b):
    ''' multiply two numbers and return the result '''
    return a * b
# Side effects can be callables.
mock = Mock(side_effect=multiplier)
# Arguments passed to the mock are passed through to the callable.
assert mock(10, 10) == 100
###############################################################################
print('No assertion errors')
```

---

## Attributes
Mock objects allow attributes to be set when created using keyword arguments. Attributes can also be set after an object is created.

Mocks create attributes dynamically when accessed if they don't already exist. Removed attributes are not dynamically recreated on subsequent attempts to access.

```python
from unittest.mock import Mock
def connection(db):
    ''' A function used to demonstrate conditional attribute access. '''
    if hasattr(db, 'connection_source'):
        return db.connection_source
    return 'xyz'
# Attributes can be set by specifying attribute names as keyword arguments.
mock = Mock(connection_source='abc', hostname='localhost')
assert mock.connection_source == 'abc'
assert mock.hostname == 'localhost'
# Attributes can also be set directly on the mock object.
mock.another_attribute = 3.14
assert mock.another_attribute == 3.14
# Attempting to access a non-existent attribute will dynamically create it.
# Attributes are mock objects.
# Assert that the created attribute exists 
assert mock.now_i_exist
# The connection function checks for an attribute named 
# connection_source on the provided object.
# If the attribute exists it's returned, otherwise 'xyz' is returned.
assert connection(mock) == 'abc'
# Remove the connection_source attribute from the mock.
del mock.connection_source
# The connection function will return xyz now that the connection_source
# attribute is set.
assert connection(mock) == 'xyz'
try:
    # Attempting to access the attribute now will raise an AttributeError.
    # Mock doesn't dynamically re-add the attribute when accessed 
    # after the attribute is deleted.
    mock.connection_source
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Removed attributes can be re-added by setting them directly.
mock.connection_source = 'welcome back'
assert mock.connection_source == 'welcome back'
###############################################################################
print('No assertion errors')
```

---

## Existing Objects
Mock objects create attributes and methods on-demand giving them the ability to replace other objects. Allowing for maximum flexibility, mocks don't enforce restrictions on allowed attributes or callable parameters. These allowed differences can lead to tests which are tightly coupled to mock objects rather than the objects being mocked.

The unittest.mock module includes mechanisms used to ensure mock objects adhere more closely to the object being mocked.

```python
from unittest.mock import MagicMock, create_autospec
class KeepingItClassy:
    def add(self, a, b):
        return self.a + self.b
    def mul(self, a, b):
        return self.a + self.b
# The spec keyword argument ensures mock matches the methods and attributes of
# a class or object.
mock = MagicMock(spec=KeepingItClassy)
# Set the return values for the two methods.
mock.add.return_value = 2
mock.mul.return_value = 10
# Calling the methods returns the expected pre-set return values.
assert mock.add(1, 1) == 2
assert mock.mul(5, 2) == 10
# Ensure the methods are called with the expected arguments.
mock.add.assert_called_with(1, 1)
mock.mul.assert_called_with(5, 2)
# Spec ensures that non-existent attributes and methods aren't created dynamically.
# Attempting to access a non-existent attributes raises an AttributeError.
try:
    mock.non_existent_attr
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Attempting to access an non-existent method raises an AttributeError.
try:
    mock.div(10, 2)
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Spec is useful for ensuring that attributes and methods match the given spec object.
# However, spec allows callables to be called with any arguments without considering 
# the defined parameters of the callable.
# A function with 2 required positional arguments.
def add(a, b):
    return a + b
# Use the add function as the spec with a return value of 2.
mock = MagicMock(spec=add, return_value=2)
assert mock(1, 1) == 2
# The spec doesn't respect the 2 defined parameters.
mock(1, 1, 1)
# The create_autospec callable creates mocks that enforce callable signatures.
# create_autospec creates a MagicMock by default.
mock = create_autospec(spec=add, return_value=2)
assert mock(1, 1) == 2
# Trying to call the mock object with the incorrect signature results in an error.
try:
    mock(1, 1, 1)
except TypeError as ex:
    print(ex)
###############################################################################
print('No assertion errors')
```

---

## Unittest
Mock objects commonly replace external resources and services. Imagine functionality is built around a callable that connects to a REST API, transforms the data, and returns the results to the caller. The REST API shouldn't be required in order to test the surrounding functionality.

The below code demonstrates using a mock to replace the ```resource_finder``` callable which simulates returning data from an external service.

```python
import random
import unittest
from unittest.mock import Mock
# Imagine that this connects out to some external source and returns resource info.
def resource_finder(ref: str, source: str) -> dict:
    return {'ref': ref, 'source': source, 'price': random.random() * random.randint(1, 10) }
class PriceLocator:
    def price_of(self, ref: str, source: str, finder: callable = resource_finder) -> float:
        ''' Simulate returning a price for a fake resource. '''
        return finder(ref, source)['price']
class PriceLocatorTestCase(unittest.TestCase):
    def test_price_of(self):
        # Setup the finder callable's method arguments.
        ref, source = 'abc123', 'amazon.com'
        price = PriceLocator()
        # External resources are not always fast, predictable, or reliable.
        # Replacing external resources inside unit tests with mocks makes tests faster and more reliable.
        # In this test knowing that the finder callable is provided with the correct arguments
        # is more important than connecting to the "external service" simulated with resource_finder.
        # This allows the price_of method to be tested independently of dependent services.
        #
        # Create a mock to replace the callable-finder argument of the price_of method.
        finder = Mock(return_value={'ref': ref, 'source': source, 'price': 3.14 })
        # Ensure the correct price is returned.
        assert price.price_of(ref, source, finder) == 3.14        
        # Ensure the finder callable was called with the expected arguments.
        finder.assert_called_with(ref, source)
if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
```

---

## Summary
The [unittest.mock](https://docs.python.org/3/library/unittest.mock.html#) module is Python's built-in mocking and patching module. Used to replace objects with fake implementations during testing.

[Mock](https://docs.python.org/3.8/library/unittest.mock.html#unittest.mock.Mock) objects are callable. Mocks can return objects and trigger side effects when called.

Mocks record calls allowing assertions to be made regarding the usage of calls. Calls can be inspected closer through attributes on the mock object. Recorded calls can also be compared using the [unittest.mock.call](https://docs.python.org/3.8/library/unittest.mock.html#call) callable.

Keep Learning: [Introduction to Patching](https://platform.qa.com/lab/python-unittest-patch/)

Code is commonly tightly coupled to external resources and services, making it more challenging to leverage mocks.

The below code demonstrates a function calling the built-in print callable. Testing this code poses a challenge because the ```greeter``` function depends on ```print``` which writes data to standard output by default.