# Solution: Control Flow and Conditionals

def is_even(n):
    return n % 2 == 0

def max_of_three(a, b, c):
    return max(a, b, c)

def categorize_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def in_range_inclusive(x, low, high):
    return low <= x <= high