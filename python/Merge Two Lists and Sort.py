list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list1 + list2
result.sort()

print("Merged and Sorted List:", result)
