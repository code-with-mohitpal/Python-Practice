t = tuple(map(int, input("Enter tuple elements: ").split()))

even = ()
odd = ()

for i in t:
    if i % 2 == 0:
        even += (i,)
    else:
        odd += (i,)

print("Even Tuple:", even)
print("Odd Tuple:", odd)
