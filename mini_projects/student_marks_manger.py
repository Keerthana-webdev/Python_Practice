students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Topper
topper = max(students, key=students.get)
print("Topper:", topper)

# Average
avg = sum(students.values()) / len(students)
print("Average:", avg)