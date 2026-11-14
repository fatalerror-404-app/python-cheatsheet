"""18. Clean Python Patterns — Unpacking"""

first, second = [10, 20]
head, *middle, tail = [1, 2, 3, 4, 5]

a = [1, 2]
b = [3, 4]
combined = [*a, *b]
