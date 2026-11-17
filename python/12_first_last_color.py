colors = []

count = int(input("Enter the number of colors: "))
print("Enter the colors:")

for _ in range(count):
    colors.append(input())

if colors:
    print("First color:", colors[0])
    print("Last color:", colors[-1])
else:
    print("No colors were entered.")
