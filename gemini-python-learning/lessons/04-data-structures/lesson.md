# Lesson 04: Data Structures in Python

## Introduction
In this lesson, we will explore the fundamental data structures available in Python. Understanding these data structures is crucial for effective programming, as they allow us to organize and manipulate data efficiently.

## Learning Objectives
By the end of this lesson, you will be able to:
- Understand the differences between lists, tuples, sets, and dictionaries.
- Use each data structure appropriately based on the requirements of your program.
- Perform common operations such as adding, removing, and accessing elements.

## Data Structures Overview

### 1. Lists
Lists are ordered collections that can hold a variety of object types. They are mutable, meaning you can change their content.

**Example:**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')  # Adding an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

### 2. Tuples
Tuples are similar to lists but are immutable. Once created, their content cannot be changed.

**Example:**
```python
coordinates = (10.0, 20.0)
print(coordinates[0])  # Output: 10.0
```

### 3. Sets
Sets are unordered collections of unique elements. They are useful for membership testing and eliminating duplicate entries.

**Example:**
```python
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # Output: {1, 2, 3}
```

### 4. Dictionaries
Dictionaries are collections of key-value pairs. They are mutable and allow for fast lookups based on keys.

**Example:**
```python
student = {'name': 'Alice', 'age': 25}
print(student['name'])  # Output: Alice
```

## Conclusion
Data structures are essential for organizing data in Python. In the next section, you will have the opportunity to practice what you've learned through a series of challenges.