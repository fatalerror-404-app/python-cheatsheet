"""12. Object-Oriented Programming — Class, object, attributes, and methods"""

class Person:
    species = "Human"  # class attribute

    def __init__(self, name, age):
        self.name = name      # instance attributes
        self.age = age

    def introduce(self):
        return f"I'm {self.name}, age {self.age}."

person = Person("Sam", 22)
person.introduce()
