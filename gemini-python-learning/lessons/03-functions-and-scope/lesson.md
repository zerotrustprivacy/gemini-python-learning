# Functions and Scope in Python

In Python, functions are a fundamental building block that allows you to encapsulate code for reuse and organization. This lesson will cover the following key concepts related to functions and scope:

## What is a Function?

A function is a reusable piece of code that performs a specific task. Functions help to break down complex problems into smaller, manageable parts. You can define a function using the `def` keyword followed by the function name and parentheses.

### Example:

```python
def greet(name):
    print(f"Hello, {name}!")
```

In this example, `greet` is a function that takes one parameter, `name`, and prints a greeting.

## Parameters and Return Values

Functions can accept parameters (inputs) and can return values (outputs). You can define multiple parameters by separating them with commas.

### Example:

```python
def add(a, b):
    return a + b
```

Here, the `add` function takes two parameters, `a` and `b`, and returns their sum.

## Scope of Variables

Scope refers to the visibility of variables in different parts of your code. There are two main types of scope in Python:

1. **Local Scope**: Variables defined inside a function are local to that function and cannot be accessed outside of it.
2. **Global Scope**: Variables defined outside of any function are global and can be accessed anywhere in the code.

### Example:

```python
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print(x + y)

my_function()  # Outputs: 15
print(y)  # Raises an error: NameError: name 'y' is not defined
```

## Conclusion

In this lesson, we have explored the basics of functions and scope in Python. Understanding how to define functions, use parameters, return values, and manage variable scope is essential for writing clean and efficient code. 

Now, you are ready to practice what you've learned with the challenges in the next file!