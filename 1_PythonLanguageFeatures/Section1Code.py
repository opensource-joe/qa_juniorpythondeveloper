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