# Solution: Loops

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

def factorial(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def count_down(n):
    out = []
    while n >= 0:
        out.append(n)
        n -= 1
    return out

def filter_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result