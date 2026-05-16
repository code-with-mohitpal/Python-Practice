students = {}

while True:
    print("\nA. Add Student")
    print("B. Update Marks")
    print("C. Search Student")
    print("D. Display All")
    print("E. Exit")

    choice = input("Enter choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 'B':
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found")

    elif choice == 'C':
        name = input("Enter student name: ")
        if name in students:
            print("Marks =", students[name])
        else:
            print("Student not found")

    elif choice == 'D':
        print(students)

    elif choice == 'E':
        break

    else:
        print("Invalid choice")
