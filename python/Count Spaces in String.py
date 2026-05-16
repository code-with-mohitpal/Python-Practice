s = input("Enter a string: ")

count = 0

for ch in s:
    if ch == " ":
        count += 1

print("Number of spaces:", count)
