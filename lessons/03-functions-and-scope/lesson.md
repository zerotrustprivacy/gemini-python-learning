# Lesson 3: Functions and Scope

Functions encapsulate reusable logic.

Definition and call:
```python
def add(a, b):
    return a + b

result = add(2, 3)
```

Defaults and keywords:
```python
def greet(name, prefix="Hello"):
    return f"{prefix}, {name}!"
```

Type hints and docstrings:
```python
def area(w: float, h: float) -> float:
    """Rectangle area."""
    return w * h
```

Scope:
- Function locals are isolated.
- Pass data via parameters and returns.