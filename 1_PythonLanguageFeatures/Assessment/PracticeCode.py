# Python Class practice code 

# Create a class called Dog with the following attributes and methods:
# - Attributes: name, age
# - Methods: sit(), roll_over()

# class Dog:
#     def __init__(self, name, age): # initialize the class
#         self.name = name # class attribute
#         self.age = age # class attribute

#     def sit(self):
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         print(f"{self.name} rolled over!")
    
# my_dog = Dog("Buddy", 6) # create an instance of the class
# your_dog = Dog("Lucy", 3) # create another instance of the class

# # Call the attributes
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog's age is {my_dog.age}.")

# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog's age is {your_dog.age}.")

# # Call the methods
# my_dog.sit() # call the sit method
# my_dog.roll_over() # call the roll_over method

# your_dog.sit() # call the sit method
# your_dog.roll_over() # call the roll_over method

# ------------------------

# Exercise 9-1 and 9-2 from Python Crash Course. Page 162.

# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Create an instance called restaurant from this class.
# Then call both methods.

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"Restaurant Name: {self.restaurant_name}")
#         print(f"Cuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open!")

# my_restaurant = Restaurant("The Great Grill", "American") # create an instance of the class

# my_restaurant.describe_restaurant() # call the describe_restaurant method
# my_restaurant.open_restaurant() # call the open_restaurant method

# # Call the attributes
# print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
# print(f"My restaurant's cuisine type is {my_restaurant.cuisine_type}.")

# # Call the methods
# my_restaurant.describe_restaurant() # call the describe_restaurant method
# my_restaurant.open_restaurant() # call the open_restaurant method

# ------------------------

# Exercise 9-3 from Python Crash Course. Page 163.
# Create a class called User. Create two attributes called first_name and last_name, and then create a method called describe_user() that prints the user's name. Create another method called greet_user() that prints a greeting to the user.
# Create an instance called user from this class.

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         print(f"User's Name: {self.first_name} {self.last_name}")

#     def greet_user(self):
#         print(f"Hello, {self.first_name} {self.last_name}!")

# my_user = User("Joe", "Castle")
# new_user = User("Jane", "Doe")

# my_user.describe_user()
# my_user.greet_user()

# new_user.describe_user()
# new_user.greet_user()

# ------------------------

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return print((long_name.title()))

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# my_old_car = Car("audi", "a4", 2016) # create an instance of the class
# my_old_car.get_descriptive_name() # call the get_descriptive_name method
# my_old_car.read_odometer() # call the read_odometer method

# my_new_car = Car("subaru", "outback", 2020) # create another instance of the class
# my_new_car.get_descriptive_name() # call the get_descriptive_name method
# my_new_car.update_odometer(23) # set the odometer_reading attribute
# my_new_car.read_odometer() # call the read_odometer method

# my_new_car.increment_odometer(100) # increment the odometer_reading attribute
# my_new_car.read_odometer() # call the read_odometer method

# ------------------------
# Exercise 9-4 from Python Crash Course. Page 163.
# Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

my_restaurant = Restaurant("The Great Grill", "American") # create an instance of the class
restaurant = Restaurant("Bob's Burgers", "Italian")  # create another instance of the class 

# Call the methods
my_restaurant.describe_restaurant() # call the describe_restaurant method
restaurant.describe_restaurant() # call the describe_restaurant method
