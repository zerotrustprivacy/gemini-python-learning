# File: /gemini-python-learning/gemini-python-learning/lessons/05-file-io/lesson.md

## Lesson 05: File Input and Output in Python

In this lesson, we will explore how to handle file input and output (I/O) in Python. File I/O is essential for reading data from files and writing data to files, which is a common requirement in many applications.

### Understanding File I/O

File I/O allows you to interact with files on your computer. Python provides built-in functions to open, read, write, and close files. The basic steps for file I/O are:

1. **Opening a File**: Use the `open()` function to open a file. You can specify the mode in which you want to open the file:
   - `'r'`: Read mode (default)
   - `'w'`: Write mode (overwrites the file if it exists)
   - `'a'`: Append mode (adds to the end of the file)
   - `'b'`: Binary mode (for non-text files)

2. **Reading from a File**: Once a file is opened in read mode, you can read its contents using methods like `read()`, `readline()`, or `readlines()`.

3. **Writing to a File**: If the file is opened in write or append mode, you can write data to it using the `write()` or `writelines()` methods.

4. **Closing a File**: It is important to close a file after you are done with it using the `close()` method to free up system resources.

### Example: Reading and Writing Files

Here’s a simple example demonstrating how to read from and write to a text file:

```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a file I/O example.\n')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Key Points to Remember

- Always close files after opening them to prevent memory leaks.
- Use the `with` statement to handle files, which automatically closes the file for you.
- Be cautious when using write mode, as it will overwrite existing files.

### Conclusion

In this lesson, we covered the basics of file input and output in Python. You learned how to open, read, write, and close files. Understanding file I/O is crucial for many programming tasks, and you will apply this knowledge in the upcoming challenges.

Now, let's move on to the exercises in the `challenge.py` file to practice what you've learned!