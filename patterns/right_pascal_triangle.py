n = 5

# Upper part
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Lower part
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()