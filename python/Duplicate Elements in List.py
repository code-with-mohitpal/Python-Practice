lst = list(map(int, input("Enter list elements: ").split()))

duplicates = set()

for i in lst:
    if lst.count(i) > 1:
        duplicates.add(i)

print("Duplicate elements:", duplicates)
