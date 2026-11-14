"""18. Clean Python Patterns — Safe dictionary lookup"""

settings = {"theme": "dark"}
theme = settings.get("theme", "light")
