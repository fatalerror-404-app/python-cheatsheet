"""18. Clean Python Patterns — `any()` and `all()`"""

has_adult = any(age >= 18 for age in [12, 17, 21])
everyone_passed = all(mark >= 50 for mark in [65, 72, 80])
