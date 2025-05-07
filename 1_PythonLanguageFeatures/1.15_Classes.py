# Introduction to Classes in Python

# Attributes define some meaningful aspect of the concept.
# Methods define some menaingful behavior of the concept.

# Classes allow for two types of attributes:
# 1. Class attributes: define attributes which apply to the type itself.
# 2. Define attributes which are isolated to each instance of an object.

class Greeter:
    default_greeting = 'Hey' # class attribute

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'{Greeter.default_greeting}, {self.name}!')

# Takeaways:
# 1. Classes are templates for creating new types of objects.
# 2. Classes can includes two types of attributes: class attributes and instance attributes.
# 3. Classes can include two types of methods: class methods and instance methods.
# 4. Classes can define a constructor by using the __init__ method.