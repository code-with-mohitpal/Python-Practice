list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

set1 = set(list1)
set2 = set(list2)

if set1.isdisjoint(set2):
    print("No common elements")
else:
    print("Lists share common elements")
