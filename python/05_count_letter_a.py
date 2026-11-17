names = []
a_count = 0

n = int(input("Enter the number of first names: "))
print("Enter the names:")

for _ in range(n):
    names.append(input())

for name in names:
    a_count += name.lower().count("a")

print("Number of a:", a_count)
