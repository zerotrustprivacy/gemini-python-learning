def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def greet_user(name):
    """Return a greeting message for the user."""
    return f"Hello, {name}!"

def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Example usage
if __name__ == "__main__":
    # Test the add_numbers function
    result_add = add_numbers(5, 3)
    print(f"Addition Result: {result_add}")  # Expected: 8

    # Test the multiply_numbers function
    result_multiply = multiply_numbers(4, 7)
    print(f"Multiplication Result: {result_multiply}")  # Expected: 28

    # Test the greet_user function
    greeting = greet_user("Alice")
    print(greeting)  # Expected: "Hello, Alice!"

    # Test the calculate_area_of_rectangle function
    area = calculate_area_of_rectangle(10, 5)
    print(f"Area of Rectangle: {area}")  # Expected: 50