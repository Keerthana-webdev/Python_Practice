students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Name: ")
    marks = int(input("Marks: "))
    students.append((name, marks))

# Sort by marks
students.sort(key=lambda x: x[1], reverse=True)

print("\nSorted List:")
for s in students:
    print(s)