# Contents of /gemini-python-learning/gemini-python-learning/Lessons/Lesson2/solution.py

# Solution to the Lesson 2 Challenge: Control Structures

# Assume the challenge was to determine if a number is even or odd and print a message accordingly.

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Example usage
if __name__ == "__main__":
    test_number = 10  # You can change this number to test other values
    result = check_even_odd(test_number)
    print(result)