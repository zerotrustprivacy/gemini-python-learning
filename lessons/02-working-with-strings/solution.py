# Solution: Working with Strings

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def format_string(name, age):
    return f"My name is {name} and I am {age} years old."