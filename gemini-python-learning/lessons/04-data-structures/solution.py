# Official solutions to the data structure exercises

# 1. List Operations
# Given a list of numbers, calculate the sum and average.

numbers = [10, 20, 30, 40, 50]

# Calculate sum
total_sum = sum(numbers)

# Calculate average
average = total_sum / len(numbers)

print(f"Sum: {total_sum}, Average: {average}")

# 2. Dictionary Manipulation
# Create a dictionary and demonstrate adding, updating, and retrieving values.

student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science"]
}

# Adding a new course
student["courses"].append("History")

# Updating age
student["age"] = 22

# Retrieving information
print(f"Student Name: {student['name']}, Age: {student['age']}, Courses: {student['courses']}")

# 3. Set Operations
# Demonstrate basic set operations: union, intersection, and difference.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a | set_b

# Intersection
intersection_set = set_a & set_b

# Difference
difference_set = set_a - set_b

print(f"Union: {union_set}, Intersection: {intersection_set}, Difference: {difference_set}")

# 4. Tuple Usage
# Create a tuple and demonstrate accessing its elements.

coordinates = (10.0, 20.0)

# Accessing elements
x, y = coordinates
print(f"X: {x}, Y: {y}")