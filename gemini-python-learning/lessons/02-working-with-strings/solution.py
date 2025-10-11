def string_length(s):
    """Return the length of the given string."""
    return len(s)

def string_concatenation(s1, s2):
    """Concatenate two strings and return the result."""
    return s1 + s2

def string_replacement(s, old, new):
    """Replace occurrences of 'old' with 'new' in the string."""
    return s.replace(old, new)

def string_uppercase(s):
    """Convert the string to uppercase."""
    return s.upper()

def string_lowercase(s):
    """Convert the string to lowercase."""
    return s.lower()

def string_split(s, delimiter=" "):
    """Split the string into a list using the specified delimiter."""
    return s.split(delimiter)

# Example usage
if __name__ == "__main__":
    sample_string = "Hello, World!"
    
    print("Original String:", sample_string)
    print("Length:", string_length(sample_string))
    print("Concatenation:", string_concatenation(sample_string, " How are you?"))
    print("Replacement:", string_replacement(sample_string, "World", "Python"))
    print("Uppercase:", string_uppercase(sample_string))
    print("Lowercase:", string_lowercase(sample_string))
    print("Split:", string_split(sample_string, ","))