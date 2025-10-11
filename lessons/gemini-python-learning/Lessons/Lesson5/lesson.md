# Lesson 5: File Handling and Exceptions

Welcome to Lesson 5! In this lesson, we will explore file handling and how to manage exceptions in Python. These skills are essential for working with data stored in files and ensuring your programs can handle errors gracefully.

## File Handling

File handling in Python allows you to read from and write to files. You can open a file using the `open()` function, which requires the name of the file and the mode in which you want to open it. The most common modes are:

- `'r'`: Read (default mode)
- `'w'`: Write (overwrites the file if it exists)
- `'a'`: Append (adds to the end of the file)
- `'b'`: Binary mode (for binary files)

### Example: Writing to a File

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.")
```

### Example: Reading from a File

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## Exception Handling

Exceptions are errors that occur during the execution of a program. Python provides a way to handle these errors using `try` and `except` blocks. This allows your program to continue running even if an error occurs.

### Example: Handling Exceptions

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
```

In this example, if the file does not exist, the program will print a message instead of crashing.

Now, head over to `challenge.py` to practice what you've learned about file handling and exceptions!