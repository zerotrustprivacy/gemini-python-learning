def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

def greet_user(name):
    """Return a greeting message for the user."""
    return f"Hello, {name}!"

def calculate_area_of_rectangle(length, width):
    """Return the area of a rectangle given its length and width."""
    return length * width

def main():
    # Test the add_numbers function
    print("Addition of 5 and 3:", add_numbers(5, 3))

    # Test the multiply_numbers function
    print("Multiplication of 4 and 2:", multiply_numbers(4, 2))

    # Test the greet_user function
    print(greet_user("Alice"))

    # Test the calculate_area_of_rectangle function
    print("Area of rectangle (5 x 3):", calculate_area_of_rectangle(5, 3))

if __name__ == "__main__":
    main()