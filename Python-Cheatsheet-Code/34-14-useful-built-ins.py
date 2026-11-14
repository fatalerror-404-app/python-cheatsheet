"""14. Useful Built-ins"""

numbers = [4, 1, 8, 2]

sorted(numbers)                    # [1, 2, 4, 8]
list(zip(["a", "b"], [1, 2]))      # [('a', 1), ('b', 2)]
list(map(str, numbers))            # ['4', '1', '8', '2']
list(filter(lambda n: n > 3, numbers))  # [4, 8]
