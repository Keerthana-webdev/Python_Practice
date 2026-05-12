n = 5

# Upper part
for i in range(1, n + 1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)

# Lower part
for i in range(n, 0, -1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)