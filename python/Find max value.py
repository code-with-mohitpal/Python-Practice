d = {'a': 10, 'b': 50, 'c': 30}

max_key = max(d, key=d.get)

print("Key with max value:", max_key)
