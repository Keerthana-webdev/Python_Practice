import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Ram", "Sam", "John", "Anu"],
    "Marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

# Add Grade column
def grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(grade)

# Analysis
print("Average:", df["Marks"].mean())
print("Topper:", df.loc[df["Marks"].idxmax()])

# Save to CSV
df.to_csv("students.csv", index=False)

# Graph
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()