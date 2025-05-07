# Introduction to Modules and Packages in Python

# Scripts are common means of automating tasks.
# A module is a file containing Python code. It can define functions, classes, and variables.
# A package is a way of organizing related modules into a single directory hierarchy.

# Use urlib to fetch a response from https://cloudacademy.com
import urllib.request
response = urllib.request.urlopen('https://cloudacademy.com')
html = response.read()
print(html[:100])  # Print the first 100 bytes of the response

# Takeaways:
# 1. A module is a collection of reusable object types which share a purpose including os, sys, and datetime.
# 2. A package is a collection of modules which share a purpose, for example, the urlib package contains multiple related modules.

# -----------------

# Exploring Modules and Packages

# create a blackjack game
def blackjack():
    # import the random module
    import random

    # create a deck of cards
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    # deal two cards to the player and the dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # show the player's hand and one of the dealer's cards
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")

blackjack()

# Use dir to list the attributes of a module.

# Takeaways:
# 1. To create a module, all you need to do is create a Python code file containing reusable code.
# 2. To create a package, all you need to do is create a folder containing modules and the special init Python file.
# 3. The Python runtime knows how to locate packages and modules by checking for folders specified in a special path setting.
# 4. The built-in dir function can be used to list the attributes of a module.
# 5. To import modules, import the entire module or specific functions from the module.

# -----------------

# A Tour of the Standard Library

# The sys module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
# The os module provides a portable way of using operating system-dependent functionality like reading or writing to the file system.
# The math module provides access to mathematical functions like sin, cos, and tan.
# The collections module provides alternatives to built-in types like lists and dictionaries.
# The random module implements pseudo-random number generators for various distributions.
# The datetime module supplies classes for manipulating dates and times.

# Takeaways:
# 1. The purpose of the standard library is to provide developers with commonly required, generally useful object types.
# 2. The sys module provides objects used to interact with the Python runtime.
# 3. The os module provides objects used to interact with the operations system where the code is running.
# 4. The math module provides access to mathematical functions.
# 5. The collections module provides alternatives to built-in types.
# 6. The random module implements pseudo-random number generators.

# In the interpreter, you can use the help function to get help on a module or function.
# For example, help(math) will give you help on the math module.
# You can also use help(math.sqrt) to get help on the sqrt function in the math module.

help()