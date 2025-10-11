# Lesson 4: Data Structures

In this lesson, we will explore some of the most commonly used data structures in Python: lists, tuples, and dictionaries. Understanding these data structures is essential for organizing and managing data effectively in your programs.

## Lists

A list is an ordered collection of items that can be changed (mutable). You can create a list by placing items inside square brackets (`[]`), separated by commas.

```python
fruits = ["apple", "banana", "cherry"]
```

You can access items in a list using their index (starting from 0).

```python
print(fruits[0])  # Output: apple
```

## Tuples

A tuple is similar to a list, but it is immutable, meaning you cannot change its contents after creation. You create a tuple by placing items inside parentheses (`()`), separated by commas.

```python
coordinates = (10, 20)
```

You can access items in a tuple just like in a list.

```python
print(coordinates[1])  # Output: 20
```

## Dictionaries

A dictionary is a collection of key-value pairs. You create a dictionary by placing items inside curly braces (`{}`), with keys and values separated by a colon (`:`).

```python
student = {
    "name": "Alex",
    "age": 25,
    "courses": ["Math", "Science"]
}
```

You can access values in a dictionary using their keys.

```python
print(student["name"])  # Output: Alex
```

## Summary

- **Lists** are mutable and ordered collections.
- **Tuples** are immutable and ordered collections.
- **Dictionaries** are mutable collections of key-value pairs.

Now, head over to `challenge.py` to practice what you've learned!