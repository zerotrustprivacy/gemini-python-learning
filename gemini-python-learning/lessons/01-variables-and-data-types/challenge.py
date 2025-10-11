# Challenge Exercises for Variables and Data Types

# Exercise 1: Variable Assignment
# Create a variable named `my_integer` and assign it the value of 10.
# Create a variable named `my_float` and assign it the value of 10.5.
# Create a variable named `my_string` and assign it the value of "Hello, World!".
# Print all three variables.

my_integer = 10
my_float = 10.5
my_string = "Hello, World!"

print("Integer:", my_integer)
print("Float:", my_float)
print("String:", my_string)

# Exercise 2: Type Checking
# Use the `type()` function to check the type of each variable created above.
# Print the type of each variable.

print("Type of my_integer:", type(my_integer))
print("Type of my_float:", type(my_float))
print("Type of my_string:", type(my_string))

# Exercise 3: Simple Arithmetic
# Create two variables, `a` and `b`, and assign them integer values.
# Calculate the sum, difference, product, and quotient of `a` and `b`.
# Print the results.

a = 15
b = 5

sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)

# Exercise 4: String Manipulation
# Create a variable `name` and assign it your name as a string.
# Create a greeting message using string concatenation.
# Print the greeting message.

name = "Your Name"
greeting = "Hello, " + name + "!"
print(greeting)

# Self-checking mechanism
# Ensure that the output matches the expected results.
expected_integer = 10
expected_float = 10.5
expected_string = "Hello, World!"
assert my_integer == expected_integer, "my_integer does not match expected value."
assert my_float == expected_float, "my_float does not match expected value."
assert my_string == expected_string, "my_string does not match expected value."
assert sum_result == 20, "Sum does not match expected value."
assert difference_result == 10, "Difference does not match expected value."
assert product_result == 75, "Product does not match expected value."
assert quotient_result == 3, "Quotient does not match expected value."
assert greeting == "Hello, Your Name!", "Greeting does not match expected value."