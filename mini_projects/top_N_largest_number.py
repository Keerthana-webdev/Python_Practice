n = input("Enter numbers: ")

# Convert string to list of integers
nums = list(map(int, n.split(",")))

# Sort in descending order
nums.sort(reverse=True)

# Print top 3
print(nums[:3])