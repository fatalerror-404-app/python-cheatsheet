"""10. File Handling"""

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
