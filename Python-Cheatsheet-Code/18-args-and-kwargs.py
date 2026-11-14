"""8. Functions — `*args` and `**kwargs`"""

def total(*numbers):
    return sum(numbers)

total(1, 2, 3)     # 6

def show_profile(**details):
    for key, value in details.items():
        print(key, value)

show_profile(name="Sam", role="Developer")
