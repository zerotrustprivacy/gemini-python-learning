# String Manipulation in Python

In this lesson, we will explore string manipulation in Python. Strings are one of the most commonly used data types in programming, and Python provides a rich set of methods and techniques for working with them.

## What is a String?

A string is a sequence of characters enclosed in quotes. In Python, you can create strings using single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

```python
# Examples of strings
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = '''This is a multi-line string.'''
```

## String Methods

Python provides many built-in methods for string manipulation. Here are some commonly used methods:

1. **`len()`**: Returns the length of the string.
   ```python
   message = "Hello"
   print(len(message))  # Output: 5
   ```

2. **`lower()`**: Converts all characters in the string to lowercase.
   ```python
   print(message.lower())  # Output: hello
   ```

3. **`upper()`**: Converts all characters in the string to uppercase.
   ```python
   print(message.upper())  # Output: HELLO
   ```

4. **`strip()`**: Removes leading and trailing whitespace.
   ```python
   spaced_string = "   Hello   "
   print(spaced_string.strip())  # Output: Hello
   ```

5. **`replace(old, new)`**: Replaces occurrences of a substring with another substring.
   ```python
   new_message = message.replace("Hello", "Hi")
   print(new_message)  # Output: Hi
   ```

6. **`split(separator)`**: Splits the string into a list based on a separator.
   ```python
   sentence = "Python is fun"
   words = sentence.split(" ")
   print(words)  # Output: ['Python', 'is', 'fun']
   ```

7. **`join(iterable)`**: Joins elements of an iterable into a single string with a specified separator.
   ```python
   words = ['Python', 'is', 'fun']
   joined_string = " ".join(words)
   print(joined_string)  # Output: Python is fun
   ```

## String Formatting

String formatting allows you to create strings dynamically. Python provides several ways to format strings:

1. **f-strings (Python 3.6+)**: Allows you to embed expressions inside string literals.
   ```python
   name = "Alice"
   greeting = f"Hello, {name}!"
   print(greeting)  # Output: Hello, Alice!
   ```

2. **`format()` method**: A versatile way to format strings.
   ```python
   age = 30
   formatted_string = "I am {} years old.".format(age)
   print(formatted_string)  # Output: I am 30 years old.
   ```

3. **Percent formatting**: An older method of formatting strings.
   ```python
   score = 95
   print("Your score is %d." % score)  # Output: Your score is 95.
   ```

## Conclusion

In this lesson, we covered the basics of string manipulation in Python, including string methods and formatting techniques. Understanding how to work with strings is essential for any Python programmer, as strings are used in various applications, from data processing to user interaction.

Now, let's put your knowledge to the test with some exercises in the next file!