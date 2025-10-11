# Challenge: File I/O Exercises

# Exercise 1: Write a function `write_to_file(filename, content)` that takes a filename and content as parameters and writes the content to the specified file. If the file already exists, it should overwrite the existing content.

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Exercise 2: Write a function `read_from_file(filename)` that takes a filename as a parameter and returns the content of the file. If the file does not exist, it should return an appropriate message.

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

# Exercise 3: Write a function `append_to_file(filename, content)` that takes a filename and content as parameters and appends the content to the specified file. If the file does not exist, it should create the file and then write the content.

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

# Exercise 4: Create a self-checking mechanism to test the above functions. You can use assertions to verify that the functions work as expected.

def test_file_io_functions():
    test_filename = 'test_file.txt'
    
    # Test writing to file
    write_to_file(test_filename, 'Hello, World!')
    assert read_from_file(test_filename) == 'Hello, World!'
    
    # Test appending to file
    append_to_file(test_filename, '\nAppending this line.')
    assert read_from_file(test_filename) == 'Hello, World!\nAppending this line.'
    
    # Test reading from a non-existent file
    assert read_from_file('non_existent_file.txt') == "File not found."
    
    print("All tests passed!")

# Uncomment the line below to run the self-checking mechanism
# test_file_io_functions()