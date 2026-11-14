"""12. Object-Oriented Programming — Class methods and static methods"""

class Temperature:
    unit = "Celsius"

    @classmethod
    def set_unit(cls, unit):
        cls.unit = unit

    @staticmethod
    def celsius_to_fahrenheit(value):
        return (value * 9 / 5) + 32
