"""10. File Handling — JSON"""

import json

data = {"name": "Sam", "active": True}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
