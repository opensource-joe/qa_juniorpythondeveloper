# Introduction to Callables

# Calling a method will run the method's code.
# Callables are named pieces of code that will run when called.
# Where condition statements are used to make decisions, callables are used for taking action.
# Callables consist of input, action, and output.

# Functions allow developers to create individual units of code that serve a developer-defined purpose.
# Function syntax is composed of the 'def' keyword, followed by the name of the function.
# The name defines the purpose of the function.

# Input into function is defined by parameters.
# Parameters are defined in parentheses after the function name.
# Parameters are separated by commas.
# Parameters are optional.

# Arguments are the values passed into the function when it is called.
# Arguments are the input used to call a callable.

# Takeaways:
# 1. A callable is a concept based on idea of input, action, and output.
# 2. Python includes different syntax for creating callables, depending on their use case.
# 3. Two types of callables are 'methods' and 'functions'.
# 4. The syntax for calling a callable is to specify the name of the callable followed by a set of parentheses containing any required input.

# Example of a function with input from user
def greet_user():
    """Greet the user with their name."""
    name = input("What is your name? ")
    print(f"Hello, {name}!")

# Call the function
greet_user()