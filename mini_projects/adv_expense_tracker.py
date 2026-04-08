import pandas as pd
import matplotlib.pyplot as plt

# Add new expense
name = input("Enter item: ")
amount = int(input("Enter amount: "))
category = input("Enter category: ")

new_data = pd.DataFrame({
    "Item": [name],
    "Amount": [amount],
    "Category": [category]
})

# Save
try:
    df = pd.read_csv("expenses.csv")
    df = pd.concat([df, new_data], ignore_index=True)
except:
    df = new_data

df.to_csv("expenses.csv", index=False)

# Analysis
print("\nTotal Spending:", df["Amount"].sum())
print("\nCategory-wise:")
print(df.groupby("Category")["Amount"].sum())

# Pie chart
df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct='%1.1f%%')
plt.title("Expenses Distribution")
plt.show()