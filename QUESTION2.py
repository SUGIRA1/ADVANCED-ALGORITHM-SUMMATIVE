def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        combined = spaces + hashes
        print(combined)

# Test case 1
staircase(6)

# Test case 2
staircase(10)
