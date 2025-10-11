# Lesson 2: Working with Strings

Strings are sequences of characters with slicing and methods.

Basics:
```python
s = "Python"
s[0], s[-1], s[1:4], len(s)
```

Common methods:
```python
" hi ".strip()
"hi".upper()
"HI".lower()
"te,st".replace(",", "")
"a,b,c".split(",")
"-".join(["a","b"])
```

Search and count:
```python
"banana".count("a")
"banana".find("na")
```

Formatting:
```python
name, age = "Ada", 30
f"Name: {name}, Age: {age}"
```