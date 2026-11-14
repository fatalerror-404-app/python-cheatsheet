"""18. Clean Python Patterns — Sorting with a key"""

users = [{"name": "Zoe", "age": 20}, {"name": "Ali", "age": 18}]
users_by_age = sorted(users, key=lambda user: user["age"])
