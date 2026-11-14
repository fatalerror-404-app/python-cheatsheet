"""7. Comprehensions"""

squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]

names = ["ada", "grace"]
capitalized = [name.title() for name in names]

lookup = {n: n * n for n in range(5)}
unique_lengths = {len(word) for word in ["cat", "bird", "dog"]}

# Generator expression: values are produced lazily
square_stream = (n * n for n in range(100))
