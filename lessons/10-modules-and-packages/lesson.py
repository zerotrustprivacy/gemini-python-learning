# Lesson 10: Modules and Packages

# Modules are Python files; packages are directories with modules (and usually __init__.py).

Import forms:

import math
from math import sqrt, pi
import random as rnd


# Using standard library modules:

import json
data = json.loads('{"a": 1}')


# Working with packages:
- Organize code into folders.
- Use relative imports inside packages: from .utils import helper