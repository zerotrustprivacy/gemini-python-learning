# Challenge for Working with Strings

# Exercise 1: String Reversal
# Write a function `reverse_string(s)` that takes a string `s` and returns the string reversed.
def reverse_string(s):
    return s[::-1]

# Exercise 2: Count Vowels
# Write a function `count_vowels(s)` that takes a string `s` and returns the number of vowels in the string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Exercise 3: Palindrome Check
# Write a function `is_palindrome(s)` that checks if the string `s` is a palindrome (reads the same forwards and backwards).
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Exercise 4: String Formatting
# Write a function `format_string(name, age)` that takes a name and age and returns a formatted string.
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

# Self-checking mechanism
if __name__ == "__main__":
    # Test reverse_string
    print(reverse_string("hello"))  # Expected: "olleh"

    # Test count_vowels
    print(count_vowels("hello world"))  # Expected: 3

    # Test is_palindrome
    print(is_palindrome("A man a plan a canal Panama"))  # Expected: True

    # Test format_string
    print(format_string("Alice", 30))  # Expected: "My name is Alice and I am 30 years old."