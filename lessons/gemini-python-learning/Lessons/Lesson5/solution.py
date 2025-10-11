# Contents of /gemini-python-learning/gemini-python-learning/Lessons/Lesson5/solution.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Writing to a file
    write_result = write_file('example.txt', 'Hello, this is a test.')
    print(write_result)

    # Reading from a file
    read_result = read_file('example.txt')
    print(read_result)