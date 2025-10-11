# lesson.md

# Lesson 01: Variables and Data Types

## Introduction
In Python, variables are used to store information that can be referenced and manipulated in a program. Understanding variables and data types is fundamental to programming, as they form the building blocks of any Python application.

## What is a Variable?
A variable is a name that refers to a value. It allows you to store data and retrieve it later. In Python, you can create a variable by simply assigning a value to it using the equals sign (`=`).

### Example:
```python
# Creating a variable
age = 25
name = "Alice"
is_student = True
```

## Data Types
Python has several built-in data types, including:

1. **Integers**: Whole numbers, e.g., `5`, `-10`.
2. **Floats**: Decimal numbers, e.g., `3.14`, `-0.001`.
3. **Strings**: Text data, e.g., `"Hello, World!"`.
4. **Booleans**: Represents `True` or `False`.

### Example:
```python
# Different data types
integer_value = 10          # Integer
float_value = 3.14         # Float
string_value = "Python"     # String
boolean_value = False       # Boolean
```

## Type Checking
You can check the type of a variable using the `type()` function.

### Example:
```python
print(type(age))          # Output: <class 'int'>
print(type(name))         # Output: <class 'str'>
```

## Type Conversion
You can convert between different data types using built-in functions like `int()`, `float()`, and `str()`.

### Example:
```python
# Type conversion
num_str = "100"
num_int = int(num_str)    # Convert string to integer
print(num_int)            # Output: 100
```

## Conclusion
Understanding variables and data types is crucial for writing effective Python code. In this lesson, we covered the basics of variables, the different data types available in Python, and how to check and convert types. 

Now, let's put this knowledge to the test with some challenges!