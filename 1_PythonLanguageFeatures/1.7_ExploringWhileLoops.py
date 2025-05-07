# Exploring While Loops
# While loops are used to execute a block of code as long as a condition is true.
# They are useful when the number of iterations is not known beforehand.

# Example of a while loop with a condition
counter = 0
while counter < 5:
    print(f"Counter is: {counter}")
    counter += 1  # Increment the counter

# Example of a while loop with user input
answer = 9
guess = input("Guess the number (between 1 and 10): ")
guess = int(guess)

if guess == answer:
    print("Correct!")
else:
    print("Wrong guess. Try again.")

# Takeaways:
# 1. The purpose of a while loop is to repeat an action until some condition is met.
# 2. The condition consists of any expression which evaluates to True.
# 3. The keyword 'continue' is used to jump to the top of the loop and re-evaluate the condition. 
# 4. The keyword 'break' is used to stop the current loop.