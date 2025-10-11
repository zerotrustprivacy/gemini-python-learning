# Challenge for Lesson 2: Control Structures

# Instructions:
# Write a program that asks the user for their age and then determines if they are eligible to vote.
# A person must be at least 18 years old to vote. If they are eligible, print a message saying they can vote.
# If they are not eligible, print a message saying they cannot vote.

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")