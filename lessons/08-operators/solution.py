# Solution: Operators

def arithmetic_ops(a, b):
    return {
        "sum": a + b,
        "diff": a - b,
        "prod": a * b,
        "quot": a / b,
        "mod": a % b,
    }

def compare_ops(a, b):
    return {
        "eq": a == b,
        "ne": a != b,
        "gt": a > b,
        "lt": a < b,
        "ge": a >= b,
        "le": a <= b,
    }

def logical_ops(a_bool, b_bool):
    return {
        "and": a_bool and b_bool,
        "or": a_bool or b_bool,
        "not_a": not a_bool,
        "not_b": not b_bool,
    }

def in_inclusive_range(x, low, high):
    return low <= x <= high