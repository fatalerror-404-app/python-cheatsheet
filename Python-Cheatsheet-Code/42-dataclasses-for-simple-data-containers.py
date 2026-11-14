"""18. Clean Python Patterns — Dataclasses for simple data containers"""

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User("Sam", 22)
