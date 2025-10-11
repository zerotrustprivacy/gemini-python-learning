# Official solution for the variables and data types challenge

# Exercise 1: Declare variables of different data types
integer_var = 10  # Integer
float_var = 10.5  # Float
string_var = "Hello, World!"  # String
boolean_var = True  # Boolean

# Print the variables and their types
print("Integer Variable:", integer_var, "Type:", type(integer_var))
print("Float Variable:", float_var, "Type:", type(float_var))
print("String Variable:", string_var, "Type:", type(string_var))
print("Boolean Variable:", boolean_var, "Type:", type(boolean_var))

# Exercise 2: Type conversion
# Convert integer to float
converted_float = float(integer_var)
print("Converted Integer to Float:", converted_float, "Type:", type(converted_float))

# Convert float to integer
converted_integer = int(float_var)
print("Converted Float to Integer:", converted_integer, "Type:", type(converted_integer))

# Exercise 3: String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Exercise 4: List of variables
variables_list = [integer_var, float_var, string_var, boolean_var]
print("List of Variables:", variables_list)