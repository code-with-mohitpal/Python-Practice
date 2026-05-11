with open("names.txt", "w") as file:
    print("Enter 5 names:")
    
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

print("\nNames stored in file:\n")

with open("names.txt", "r") as file:
    content = file.read()
    print(content)
