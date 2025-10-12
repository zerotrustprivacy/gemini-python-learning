# Lesson 7: Loops

for loops iterate over sequences; while loops repeat while a condition is true.

for:
```python
nums = [1, 2, 3]
total = 0
for n in nums:
    total += n
```

range and enumerate:
```python
for i in range(5):  # 0..4
    pass

for i, val in enumerate(["a", "b", "c"], start=1):
    pass
```

while:
```python
count = 3
while count > 0:
    count -= 1
```

break, continue:
```python
for n in range(10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
```