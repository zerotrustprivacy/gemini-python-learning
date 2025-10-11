# Lesson 3: Functions and Modules

In this lesson, we will explore functions and modules in Python. Functions allow you to encapsulate code into reusable blocks, while modules help organize your code into separate files.

## What is a Function?

A function is a block of code that performs a specific task. You can define a function using the `def` keyword, followed by the function name and parentheses. You can also pass data to functions using parameters.

Here's a simple example of a function that greets a user:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

## Why Use Functions?

Functions help you avoid code duplication and make your code more organized and easier to read. You can call a function multiple times with different arguments.

## What is a Module?

A module is a file containing Python code that can define functions, classes, and variables. You can import a module into another Python file using the `import` statement.

For example, if you have a module named `math_utils.py` with a function to add two numbers:

```python
# math_utils.py
def add(a, b):
    return a + b
```

You can use this function in another file:

```python
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8
```

## Creating Your Own Functions and Modules

Now it's your turn! Create your own functions and organize them into modules. Head over to `challenge.py` to practice what you've learned!