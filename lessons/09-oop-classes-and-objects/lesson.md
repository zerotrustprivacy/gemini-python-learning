# Lesson 9: OOP — Classes and Objects

Classes define blueprints; objects are instances with state (attributes) and behavior (methods).

Basic class:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
```

Special methods:
- __init__: initializer
- __repr__/__str__: string representation

Encapsulation by convention:
- Prefix with _ for “internal” attributes.

Composition:
```python
class Engine: ...
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
```