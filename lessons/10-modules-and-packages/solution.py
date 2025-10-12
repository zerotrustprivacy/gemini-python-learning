# Solution: Modules and Packages

import math
import random
import json

def random_int_in_range(low, high):
    return random.randint(low, high)

def circle_area(radius):
    return math.pi * (radius ** 2)

def load_json_string(s):
    return json.loads(s)

def pick_random_choice(items):
    return random.choice(items)