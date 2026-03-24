# Write names to file
with open("names.txt", "w") as file:
    for i in range(5):
        name = input("Enter name: ")
        file.write(name + "\n")

# Read and print names
with open("names.txt", "r") as file:
    print("Names in file:")
    print(file.read())
