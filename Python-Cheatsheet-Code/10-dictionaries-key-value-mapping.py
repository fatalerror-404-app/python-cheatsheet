"""5. Collections — Dictionaries --- key/value mapping"""

person = {"name": "Sam", "age": 22}

person["name"]
person.get("city", "Unknown")  # safe lookup with default

person["city"] = "Lahore"
person.update({"age": 23})
person.pop("age")

person.keys()
person.values()
person.items()

for key, value in person.items():
    print(key, value)
