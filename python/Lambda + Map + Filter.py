numbers = [1, 2, 3, 4, 5, 6]

square = list(map(lambda x: x*x, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

print("Square:", square)
print("Even:", even)
