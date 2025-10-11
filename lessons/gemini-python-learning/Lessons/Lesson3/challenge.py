def calculate_area_of_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

def calculate_area_of_rectangle(length, width):
    area = length * width
    return area

def main():
    print("Area Calculator")
    
    # Circle
    radius = float(input("Enter the radius of the circle: "))
    circle_area = calculate_area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {circle_area}")

    # Rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle_area = calculate_area_of_rectangle(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area}")

if __name__ == "__main__":
    main()