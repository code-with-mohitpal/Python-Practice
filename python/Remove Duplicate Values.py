d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

unique = {}
seen = set()

for key, value in d.items():
    if value not in seen:
        unique[key] = value
        seen.add(value)

print(unique)
