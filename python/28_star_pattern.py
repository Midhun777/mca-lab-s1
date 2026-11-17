step = 5

# Print the upper part of the pattern.
for i in range(1, step + 1):
    for _ in range(i):
        print("*", end=" ")
    print()

# Print the lower part of the pattern.
for i in range(step - 1, 0, -1):
    for _ in range(i):
        print("*", end=" ")
    print()
