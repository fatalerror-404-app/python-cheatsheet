"""8. Functions — Scope and lambda"""

rate = 10

def calculate(amount):
    local_total = amount * rate
    return local_total

double = lambda number: number * 2
double(5)          # 10
