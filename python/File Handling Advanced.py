# Read and Write File

with open("student.txt", "w") as file:
    file.write("Mohit Pal\n")
    file.write("AI & ML Engineering")

with open("student.txt", "r") as file:
    content = file.read()

print(content)
