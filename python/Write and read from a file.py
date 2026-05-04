# write
with open("student.txt", "w") as f:
    name = input("Enter name: ")
    f.write(name)

# read
with open("student.txt", "r") as f:
    print("Stored Name:", f.read())
