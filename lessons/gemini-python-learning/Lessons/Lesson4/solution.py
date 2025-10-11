# Contents of /gemini-python-learning/gemini-python-learning/Lessons/Lesson4/solution.py

# Solution to the Lesson 4 Challenge: Data Structures

# Let's assume the challenge was to create a function that takes a list of numbers
# and returns a dictionary with the count of each number.

def count_numbers(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    return count_dict

# Example usage
if __name__ == "__main__":
    sample_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    result = count_numbers(sample_numbers)
    print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}