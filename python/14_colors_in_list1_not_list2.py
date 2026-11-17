colors1 = set()
colors2 = set()

n1 = int(input("Enter the number of colors in List 1: "))
print("Enter the colors for List 1:")
for _ in range(n1):
    colors1.add(input())

n2 = int(input("Enter the number of colors in List 2: "))
print("Enter the colors for List 2:")
for _ in range(n2):
    colors2.add(input())

difference = colors1.difference(colors2)
print("Colors in List 1 not in List 2:", difference)
