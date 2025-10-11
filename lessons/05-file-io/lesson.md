# Lesson 5: File I/O

Modes:
- r: read
- w: write (overwrite)
- a: append
- encoding="utf-8" for text

Examples:
```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("First\n")

with open("out.txt", "a", encoding="utf-8") as f:
    f.write("Next\n")

with open("out.txt", "r", encoding="utf-8") as f:
    content = f.read()
```