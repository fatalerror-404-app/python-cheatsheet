"""18. Clean Python Patterns — Context managers"""

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Application started\n")
