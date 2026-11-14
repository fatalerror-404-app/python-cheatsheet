"""12. Object-Oriented Programming — Inheritance and method overriding"""

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} ID: {self.student_id}"
