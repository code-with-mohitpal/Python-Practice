# Append log entry
with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

# Read and print logs
with open("log.txt", "r") as file:
    print("Logs:")
    print(file.read())
