d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 15}

result = d1.copy()

for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
