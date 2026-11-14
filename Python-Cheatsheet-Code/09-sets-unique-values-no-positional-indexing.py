"""5. Collections — Sets --- unique values, no positional indexing"""

first = {1, 2, 3}
second = {3, 4, 5}

first.add(4)
first.discard(99)      # safe if absent

first | second         # union
first & second         # intersection
first - second         # difference
first ^ second         # symmetric difference
