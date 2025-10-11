# Lesson 2: Control Structures

In this lesson, we will explore control structures in Python, which allow you to dictate the flow of your program based on certain conditions. The two main types of control structures we will cover are conditionals and loops.

## Conditionals

Conditionals let you execute certain pieces of code based on whether a condition is true or false. The most common conditional statement is the `if` statement.

### Syntax of an `if` statement:

```python
if condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another_condition is true
else:
    # code to execute if none of the above conditions are true
```

### Example:

```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")
```

## Loops

Loops allow you to execute a block of code multiple times. The two main types of loops in Python are `for` loops and `while` loops.

### `for` loop:

A `for` loop iterates over a sequence (like a list or a string).

```python
for i in range(5):
    print(i)  # Prints numbers from 0 to 4
```

### `while` loop:

A `while` loop continues to execute as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count
```

## Practice

Now that you have learned about conditionals and loops, head over to `challenge.py` to practice what you've learned!