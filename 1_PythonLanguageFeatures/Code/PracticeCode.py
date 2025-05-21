# # Code examples from section 1

# # Section 1.7: Exploring While Loops
# # Example of a while loop with a condition
# counter = 0
# while counter < 5:
#     print(f"Counter is: {counter}")
#     counter += 1  # Increment the counter

# # Example of a while loop with user input
# answer = 9
# guess = input("Guess the number (between 1 and 10): ")
# guess = int(guess)

# if guess == answer:
#     print("Correct!")
# else:
#     print("Wrong guess. Try again.")

# # Using break and continue in a while loop
# while True:
#     command = input("Enter a command (or 'exit' to quit): ")
#     if command == "exit":
#         print("Exiting the loop.")
#         break  # Exit the loop
#     elif command == "skip":
#         print("Skipping this iteration.")
#         continue  # Skip to the next iteration
#     else:
#         print(f"You entered: {command}")

# # --------------------------------
# # Section 1.8: Callables

# # Example of a function with input from user
# def greet_user():
#     """Greet the user with their name."""
#     name = input("What is your name? ")
#     print(f"Hello, {name}!")

# greet_user() # Call the function

# # Example of a function with parameters
# def add_three(a, b, c):
#     """Add three numbers."""
#     print(a + b + c)  # Print the sum of the three numbers

# add_three(1, 2, 3)  # Call the function with arguments

# # --------------------------------
# # Section 1.9: Built-in Functions

# # Print function used for displaying text in the console.
# print("Hello, World!")  # Output: Hello, World!

# # Input function used for taking user input from the console.
# user_input = input("Enter your name: ")  # Output: Enter your name: (waits for user input)
# print(f"Hello, {user_input}!")  # Output: Hello, <user_input>!

# --------------------------------

# # Section 1.12: Modules and Packages
# # Use urlib to fetch a response from https://cloudacademy.com

# import urllib.request
# response = urllib.request.urlopen('https://cloudacademy.com')
# html = response.read()
# print(html[:100])  # Print the first 100 bytes of the response

# --------------------------------

# # Section 1.14: Exception Handling

# raise Exception('Oh no, something went wrong!')  # Raise an exception with a custom message

# # Raise an Exception and pass arguments to it, but it is not raised
# broken_universe = Exception('The universe is broken', 'UNI-0435')
# print(broken_universe.args)

# # Exceptions are normal objects until they are raised.
# broken_universe = Exception('The universe is broken', 'UNI-0435')
# raise broken_universe

# # Using try, except, else, and finally to handle exceptions
# try:
#     print('from try')
# except:
#     print('from except')
# else:
#     print('from else')
# finally:
#     print('from finally')

# # The combination of try and finally provides a mechanism for perfoming cleanup actions such as closing files, network and database connections, etc.
# try:
#     f = open('dataset.txt', 'w')
#     f.write('python is neat')
# finally:
#     f.close()
#     print('file closed!')

# # The code below follows the ask for forgiveness model by attempting to open the file and handling the exception if the file is missing.
# import json

# try:
#     with open('dataset.json') as dataset:
#         ds = json.loads(dataset.read())
#         ...
# except OSError:
#     print('missing dataset file')