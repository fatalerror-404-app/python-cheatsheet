# Python Cheatsheet

### A practical, GitHub-ready reference for Python 3

> A compact reference for everyday Python: syntax, built-in data
> structures, functions, OOP, files, exceptions, useful standard-library
> tools, and development workflow.

**Version:** Python 3.x\
**Audience:** Beginner → Intermediate\
**Tip:** Run the examples in a Python 3 interpreter. Examples are
independent unless stated otherwise.

------------------------------------------------------------------------

## Contents

-   [1. Python Basics](#1-python-basics)
-   [2. Variables and Data Types](#2-variables-and-data-types)
-   [3. Operators](#3-operators)
-   [4. Strings](#4-strings)
-   [5. Collections](#5-collections)
-   [6. Control Flow](#6-control-flow)
-   [7. Comprehensions](#7-comprehensions)
-   [8. Functions](#8-functions)
-   [9. Exceptions](#9-exceptions)
-   [10. File Handling](#10-file-handling)
-   [11. Modules and Packages](#11-modules-and-packages)
-   [12. Object-Oriented Programming](#12-object-oriented-programming)
-   [13. Iterators and Generators](#13-iterators-and-generators)
-   [14. Useful Built-ins](#14-useful-built-ins)
-   [15. Standard Library Essentials](#15-standard-library-essentials)
-   [16. Type Hints](#16-type-hints)
-   [17. Virtual Environments and pip](#17-virtual-environments-and-pip)
-   [18. Clean Python Patterns](#18-clean-python-patterns)
-   [19. Quick Debugging](#19-quick-debugging)

------------------------------------------------------------------------

## 1. Python Basics

``` python
# A comment starts with #
print("Hello, Python!")

# Multiple statements
name = "Alex"
age = 21

# Indentation defines code blocks
if age >= 18:
    print("Adult")

# Get input (input() always returns a string)
user_name = input("Your name: ")
```

Run a script from the terminal:

``` bash
python main.py
# On some systems:
python3 main.py
```

Python is case-sensitive: `name`, `Name`, and `NAME` are different
identifiers.

## 2. Variables and Data Types

Python is dynamically typed. A variable refers to an object; its type is
determined at runtime.

  Type         Example                Mutable?
  ------------ -------------------- ----------
  `int`        `42`                         No
  `float`      `3.14`                       No
  `complex`    `2 + 3j`                     No
  `str`        `"Python"`                   No
  `bool`       `True`                       No
  `NoneType`   `None`                       No
  `list`       `[1, 2, 3]`                 Yes
  `tuple`      `(1, 2, 3)`                  No
  `set`        `{1, 2, 3}`                 Yes
  `dict`       `{"name": "Alex"}`          Yes

``` python
count = 10
price = 19.99
is_active = True
nothing = None

print(type(count))       # <class 'int'>
print(isinstance(price, float))  # True

# Type conversion
int("25")       # 25
float("3.5")    # 3.5
str(100)        # "100"
bool(1)         # True
list("cat")     # ['c', 'a', 't']
```

**Naming conventions:** use `snake_case` for variables/functions,
`PascalCase` for classes, and `UPPER_SNAKE_CASE` for constants.

## 3. Operators

### Arithmetic

  Operator   Meaning          Example
  ---------- ---------------- ----------------
  `+`        Addition         `8 + 2  # 10`
  `-`        Subtraction      `8 - 2  # 6`
  `*`        Multiplication   `8 * 2  # 16`
  `/`        True division    `7 / 2  # 3.5`
  `//`       Floor division   `7 // 2  # 3`
  `%`        Remainder        `7 % 2  # 1`
  `**`       Exponent         `2 ** 3  # 8`

### Comparison and logical

``` python
a == b       # equal
a != b       # not equal
a > b        # greater than
a <= b       # less than or equal

age >= 18 and has_id
is_admin or is_owner
not is_blocked
```

### Assignment and membership

``` python
x += 1       # x = x + 1
x *= 2
"py" in "python"       # True
4 not in [1, 2, 3]     # True
```

Use `is` to test object identity, especially `value is None`; use `==`
to compare values.

## 4. Strings

``` python
text = "Python is fun"

text[0]          # 'P'
text[-1]         # 'n'
text[0:6]        # 'Python'
text[::2]        # every second character
text[::-1]       # reversed string

len(text)
text.lower()
text.upper()
text.title()
text.strip()
text.replace("fun", "powerful")
text.split()                 # list of words
"-".join(["2026", "11", "14"])
text.startswith("Py")
text.endswith("fun")
```

### f-strings

``` python
name = "Sam"
score = 93.456

print(f"Hello, {name}!")
print(f"Score: {score:.2f}")   # 93.46
print(f"{1000000:,}")          # 1,000,000
```

Strings are immutable: methods return new strings rather than changing
the original.

## 5. Collections

### Lists --- ordered and mutable

``` python
numbers = [10, 20, 30]

numbers[0]             # 10
numbers[-1]            # 30
numbers[1:3]           # [20, 30]

numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
numbers.remove(30)     # removes first matching value
last = numbers.pop()   # removes and returns last item
numbers.sort()
numbers.reverse()

copy_of_numbers = numbers.copy()
```

### Tuples --- ordered and immutable

``` python
point = (10, 20)
x, y = point           # unpacking

single_item = (5,)     # comma is required
```

### Sets --- unique values, no positional indexing

``` python
first = {1, 2, 3}
second = {3, 4, 5}

first.add(4)
first.discard(99)      # safe if absent

first | second         # union
first & second         # intersection
first - second         # difference
first ^ second         # symmetric difference
```

An empty set is `set()`, not `{}` (`{}` creates an empty dictionary).

### Dictionaries --- key/value mapping

``` python
person = {"name": "Sam", "age": 22}

person["name"]
person.get("city", "Unknown")  # safe lookup with default

person["city"] = "Lahore"
person.update({"age": 23})
person.pop("age")

person.keys()
person.values()
person.items()

for key, value in person.items():
    print(key, value)
```

Dictionary keys must be hashable. Common choices include strings,
numbers, and tuples of hashable values.

## 6. Control Flow

### if / elif / else

``` python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

### for loop

``` python
for item in ["red", "green", "blue"]:
    print(item)

for number in range(1, 5):  # 1, 2, 3, 4
    print(number)

for index, value in enumerate(["a", "b"], start=1):
    print(index, value)
```

### while loop

``` python
attempts = 0

while attempts < 3:
    print("Try again")
    attempts += 1
```

### Loop control

``` python
for number in range(10):
    if number == 2:
        continue      # skip this iteration
    if number == 6:
        break         # stop the loop
    print(number)
else:
    print("Loop finished without break")
```

`pass` is a placeholder that does nothing.

## 7. Comprehensions

Create collections concisely:

``` python
squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]

names = ["ada", "grace"]
capitalized = [name.title() for name in names]

lookup = {n: n * n for n in range(5)}
unique_lengths = {len(word) for word in ["cat", "bird", "dog"]}

# Generator expression: values are produced lazily
square_stream = (n * n for n in range(100))
```

Prefer readable loops when a comprehension becomes difficult to
understand.

## 8. Functions

``` python
def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

message = greet("Sam")
```

### Parameters and return values

``` python
def power(base, exponent=2):
    return base ** exponent

power(3)          # 9
power(2, 3)       # 8
power(base=2, exponent=4)  # 16
```

### `*args` and `**kwargs`

``` python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)     # 6

def show_profile(**details):
    for key, value in details.items():
        print(key, value)

show_profile(name="Sam", role="Developer")
```

### Scope and lambda

``` python
rate = 10

def calculate(amount):
    local_total = amount * rate
    return local_total

double = lambda number: number * 2
double(5)          # 10
```

Use `lambda` for small, simple expressions; use `def` for reusable
logic.

**Avoid mutable default arguments:**

``` python
# Good: create a fresh list for each call
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 9. Exceptions

``` python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")
else:
    print("Result:", result)  # runs if no exception occurred
finally:
    print("Finished.")        # runs whether an error occurred or not
```

Raise an exception when an operation cannot proceed:

``` python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

Catch specific exceptions instead of using a broad `except:` wherever
possible.

## 10. File Handling

Use `with` so files are closed automatically.

``` python
# Write text
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file!")

# Read all text
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Read line by line
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

  Mode   Purpose
  ------ -------------------------------
  `r`    Read (file must exist)
  `w`    Write (overwrites or creates)
  `a`    Append (creates if needed)
  `x`    Create, fail if it exists
  `b`    Binary mode modifier
  `+`    Read and write modifier

### JSON

``` python
import json

data = {"name": "Sam", "active": True}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
```

## 11. Modules and Packages

``` python
import math
from pathlib import Path
import random as rnd

math.sqrt(81)
rnd.randint(1, 6)
Path("notes.txt").exists()
```

A module is a `.py` file. A package organizes modules in a directory.

``` python
# Import your own module
import helpers
helpers.greet("Sam")
```

Protect script-only code:

``` python
def main():
    print("Application starts here")

if __name__ == "__main__":
    main()
```

## 12. Object-Oriented Programming

### Class, object, attributes, and methods

``` python
class Person:
    species = "Human"  # class attribute

    def __init__(self, name, age):
        self.name = name      # instance attributes
        self.age = age

    def introduce(self):
        return f"I'm {self.name}, age {self.age}."

person = Person("Sam", 22)
person.introduce()
```

### Inheritance and method overriding

``` python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} ID: {self.student_id}"
```

### Class methods and static methods

``` python
class Temperature:
    unit = "Celsius"

    @classmethod
    def set_unit(cls, unit):
        cls.unit = unit

    @staticmethod
    def celsius_to_fahrenheit(value):
        return (value * 9 / 5) + 32
```

### Properties

``` python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
```

Python uses conventions rather than strict access modifiers: `_name`
means internal-use by convention; `__name` triggers name mangling.

## 13. Iterators and Generators

``` python
items = [10, 20, 30]
iterator = iter(items)

next(iterator)  # 10
next(iterator)  # 20
```

A generator yields values one at a time:

``` python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for value in countdown(3):
    print(value)
```

Use generators for large sequences or streams when you do not need all
values in memory at once.

## 14. Useful Built-ins

  Built-in            What it does
  ------------------- ---------------------------------
  `print()`           Display output
  `input()`           Read user input
  `type()`            Get an object's type
  `isinstance()`      Check an object's type
  `len()`             Number of items
  `range()`           Generate an integer sequence
  `enumerate()`       Pair indexes with values
  `zip()`             Iterate over iterables together
  `sorted()`          Return a new sorted list
  `reversed()`        Iterate in reverse
  `sum()`             Add numeric values
  `min()` / `max()`   Smallest / largest
  `any()` / `all()`   Test truth values
  `abs()`             Absolute value
  `round()`           Round a number
  `map()`             Apply a function to items
  `filter()`          Keep matching items

``` python
numbers = [4, 1, 8, 2]

sorted(numbers)                    # [1, 2, 4, 8]
list(zip(["a", "b"], [1, 2]))      # [('a', 1), ('b', 2)]
list(map(str, numbers))            # ['4', '1', '8', '2']
list(filter(lambda n: n > 3, numbers))  # [4, 8]
```

## 15. Standard Library Essentials

Python includes many useful modules without installing third-party
packages.

  Module          Common use
  --------------- ---------------------------------
  `math`          Mathematical functions
  `random`        Random selections and numbers
  `statistics`    Mean, median, mode
  `datetime`      Dates and times
  `time`          Time-related functions
  `pathlib`       Filesystem paths
  `os`            Operating-system interfaces
  `sys`           Interpreter/runtime information
  `json`          JSON encoding and decoding
  `csv`           CSV reading and writing
  `re`            Regular expressions
  `collections`   Specialized containers
  `itertools`     Efficient iterator tools
  `functools`     Higher-order function utilities
  `subprocess`    Run external processes
  `logging`       Application logging

### Handy examples

``` python
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

Path("reports").mkdir(exist_ok=True)
today = datetime.now()
Counter("mississippi").most_common(2)

groups = defaultdict(list)
groups["Python"].append("cheatsheet")
```

## 16. Type Hints

Type hints document expected types and help editors and static-analysis
tools. Python does not enforce them automatically at runtime.

``` python
def greeting(name: str) -> str:
    return f"Hello, {name}"

def average(values: list[float]) -> float:
    return sum(values) / len(values)

def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Sam"
    return None
```

For older Python versions, some annotations may require imports from
`typing`, such as `Optional`, `List`, and `Dict`.

## 17. Virtual Environments and pip

Create an isolated environment for each project:

``` bash
# Create
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate

# Install a package
python -m pip install requests

# List installed packages
python -m pip list

# Save dependencies
python -m pip freeze > requirements.txt

# Install project dependencies
python -m pip install -r requirements.txt

# Leave the environment
deactivate
```

Keep `.venv/` out of version control. Commit `requirements.txt` when it
is appropriate for your project.

## 18. Clean Python Patterns

### Unpacking

``` python
first, second = [10, 20]
head, *middle, tail = [1, 2, 3, 4, 5]

a = [1, 2]
b = [3, 4]
combined = [*a, *b]
```

### Sorting with a key

``` python
users = [{"name": "Zoe", "age": 20}, {"name": "Ali", "age": 18}]
users_by_age = sorted(users, key=lambda user: user["age"])
```

### Safe dictionary lookup

``` python
settings = {"theme": "dark"}
theme = settings.get("theme", "light")
```

### `any()` and `all()`

``` python
has_adult = any(age >= 18 for age in [12, 17, 21])
everyone_passed = all(mark >= 50 for mark in [65, 72, 80])
```

### Context managers

``` python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Application started\n")
```

### Dataclasses for simple data containers

``` python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User("Sam", 22)
```

## 19. Quick Debugging

``` python
# Inspect a value and its type
value = 42
print(value, type(value))

# Python debugger
breakpoint()

# Read an exception traceback carefully:
# 1. Find the final exception type and message.
# 2. Locate the line in your own code.
# 3. Check the values and types used on that line.
```

Run Python with warnings enabled:

``` bash
python -Wd main.py
```

------------------------------------------------------------------------

## Quick Reference: Common Mistakes

  -----------------------------------------------------------------------
  Avoid                               Prefer
  ----------------------------------- -----------------------------------
  `value == None`                     `value is None`

  `list = []` as a function default   `items=None`, then create the list
                                      inside

  `except:`                           Catch the specific exception

  `open()` without closing            Use `with open(...)`

  `a = b` when you need a copy        `b.copy()` for a shallow list/dict
                                      copy

  `sort()` when you need a new list   `sorted(items)`

  Comparing floats with exact         Use `math.isclose()` where
  equality                            appropriate
  
------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<b>`{=html}Keep learning. Keep building. Keep Pythonic.`</b>`{=html}
```{=html}
</p>
```
