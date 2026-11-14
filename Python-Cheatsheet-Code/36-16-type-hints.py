"""16. Type Hints"""

def greeting(name: str) -> str:
    return f"Hello, {name}"

def average(values: list[float]) -> float:
    return sum(values) / len(values)

def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Sam"
    return None
