# Solution: Data Structures

def create_shopping_list():
    return ["apples", "bananas", "bread", "milk", "eggs"]

def add_item_to_list(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

def remove_item_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

def create_student_grades():
    return {"Ada": 95, "Bob": 88, "Cara": 91}

def get_student_grade(grades_dict, student_name):
    return grades_dict.get(student_name, "Not found")