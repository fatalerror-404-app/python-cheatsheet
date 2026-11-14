"""5. Collections — Lists --- ordered and mutable"""

numbers = [10, 20, 30]

numbers[0]             # 10
numbers[-1]            # 30
numbers[1:3]           # [20, 30]

numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
numbers.remove(30)     # removes first matching value
last = numbers.pop()   # removes and returns last item
numbers.sort()
numbers.reverse()

copy_of_numbers = numbers.copy()
