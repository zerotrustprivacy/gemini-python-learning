# File: /gemini-python-learning/gemini-python-learning/lessons/05-file-io/solution.py

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

def write_file(file_path, content):
    """Writes the given content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"

def append_to_file(file_path, content):
    """Appends the given content to a file."""
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return "Content appended successfully."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Define file path
    file_path = 'example.txt'
    
    # Write to file
    write_result = write_file(file_path, "Hello, World!\n")
    print(write_result)
    
    # Append to file
    append_result = append_to_file(file_path, "Appending this line.\n")
    print(append_result)
    
    # Read from file
    file_content = read_file(file_path)
    print("File Content:\n", file_content)