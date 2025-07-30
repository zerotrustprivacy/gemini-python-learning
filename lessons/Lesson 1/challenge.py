# Challenge: Variables and Data Types
#
# Welcome to your first challenge!
# The goal of this challenge is to practice creating variables of different data types.
#
# Instructions:
# 1. Below each comment, create a variable with the specified name and data type.
# 2. Assign a value to each variable that matches its data type.
# 3. After you've created all the variables, run this file by opening a terminal
#    (Ctrl+` or Cmd+`) and typing `python "lessons/Lesson 1/challenge.py"`
#    to see the output.

# A string variable named `first_name`
# Your code here

# An integer variable named `your_age`
# Your code here

# A float variable named `account_balance`
# Your code here

# A boolean variable named `is_active_user`
# Your code here


# --- Do not modify the code below this line ---
# This code will print your variables and their types.
try:
    print(f"First Name: {first_name}, Type: {type(first_name)}")
except NameError:
    print("Variable 'first_name' is not defined.")
try:
    print(f"Your Age: {your_age}, Type: {type(your_age)}")
except NameError:
    print("Variable 'your_age' is not defined.")
try:
    print(f"Account Balance: {account_balance}, Type: {type(account_balance)}")
except NameError:
    print("Variable 'account_balance' is not defined.")
try:
    print(f"Is Active User: {is_active_user}, Type: {type(is_active_user)}")
except NameError:
    print("Variable 'is_active_user' is not defined.")