# Lesson 4: Data Structures

Lists:
```python
items = ["apple", "banana"]
items.append("cherry")
```

Tuples:
```python
point = (10, 20)
```

Sets:
```python
nums = {1, 2, 2, 3}
```

Dictionaries:
```python
grades = {"Ada": 95, "Bob": 88}
grades["Cara"] = 91
grades.get("Bob", 0)
```

Comprehensions:
```python
[n*n for n in range(5)]
{n for n in range(10) if n % 2 == 0}
{name: len(name) for name in ["Ada", "Bob"]}
```