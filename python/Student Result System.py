marks = []
for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

percentage = sum(marks) / 5

if percentage >= 90:
    grade = 'A'
elif percentage >= 75:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'Fail'

print("Percentage:", percentage)
print("Grade:", grade)
