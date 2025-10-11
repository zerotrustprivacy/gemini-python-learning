# Challenge Exercises for Data Structures

# Exercise 1: List Manipulation
# Create a list of your favorite fruits. 
# Write a function that adds a new fruit to the list and returns the updated list.

def add_fruit(fruit_list, new_fruit):
    fruit_list.append(new_fruit)
    return fruit_list

# Exercise 2: Dictionary Usage
# Create a dictionary to store the ages of three of your friends.
# Write a function that takes the dictionary and a friend's name as input and returns their age.

def get_age(friends_ages, name):
    return friends_ages.get(name, "Friend not found.")

# Exercise 3: Set Operations
# Create a set of unique colors you like.
# Write a function that takes two sets of colors and returns their intersection.

def common_colors(set1, set2):
    return set1.intersection(set2)

# Self-checking mechanism
if __name__ == "__main__":
    # Test Exercise 1
    fruits = ["apple", "banana", "cherry"]
    print("Original fruits:", fruits)
    updated_fruits = add_fruit(fruits, "orange")
    print("Updated fruits:", updated_fruits)

    # Test Exercise 2
    friends_ages = {"Alice": 25, "Bob": 30, "Charlie": 22}
    print("Alice's age:", get_age(friends_ages, "Alice"))
    print("David's age:", get_age(friends_ages, "David"))

    # Test Exercise 3
    colors1 = {"red", "green", "blue"}
    colors2 = {"blue", "yellow", "green"}
    print("Common colors:", common_colors(colors1, colors2))