# Lesson 6: Control Flow and Conditionals

Control flow determines which code runs and when. Conditionals evaluate expressions to decide different paths.

if / elif / else:
```python
x = 7
if x > 10:
    print("big")
elif x == 10:
    print("ten")
else:
    print("small")
```

Truthiness:
- Falsy: 0, 0.0, "", [], {}, set(), None, False
- Truthy: most other values

Ternary expression:
```python
msg = "even" if x % 2 == 0 else "odd"
```

match (pattern matching, Python 3.10+):
```python
status = 404
match status:
    case 200:
        kind = "ok"
    case 404:
        kind = "not found"
    case _:
        kind = "other"
```

Combine comparisons:
```python
age = 21
is_adult = age >= 18
in_range = 1 <= x <= 10
```