# Lesson 1: Variables and Data Types

Welcome to your first Python lesson! Today, we'll cover the building blocks of any program: variables and data types.

## What is a Variable?

Think of a variable as a labeled box where you can store information. You give the box a name (the variable name), and you can put things inside it (the value). You can also change what's inside the box later.

In Python, you create a variable by giving it a name and using the equals sign (`=`) to assign it a value.

```python
message = "Hello, World!"
my_favorite_number = 7
pi_approx = 3.14
```

## Common Data Types

The "type" of data is what kind of information you're storing. Python has several built-in data types, but let's start with the most common ones:

1.  **String (`str`)**: Used for text. You create a string by putting text inside single (`'`) or double (`"`) quotes.
    ```python
    student_name = "Alex"
    ```

2.  **Integer (`int`)**: Used for whole numbers (no decimals).
    ```python
    age = 25
    ```

3.  **Float (`float`)**: Used for numbers with decimal points. The name "float" comes from "floating-point number".
    ```python
    price = 19.99
    ```

4.  **Boolean (`bool`)**: Can only have one of two values: `True` or `False`. These are very important for making decisions in your code.
    ```python
    is_learning = True
    game_over = False
    ```

You can check the type of a variable using the `type()` function.

```python
print(type(student_name))  # <class 'str'>
print(type(age))           # <class 'int'>
```

Now, head over to `challenge.py` to practice what you've learned!