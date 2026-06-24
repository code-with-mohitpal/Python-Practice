numbers = [10, 25, 8, 45, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element in the list is =", largest)