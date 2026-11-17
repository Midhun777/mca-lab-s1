numbers = []

n = int(input("Enter the number of elements: "))
print("Enter the integers:")

for _ in range(n):
    value = int(input())

    if value > 100:
        numbers.append("over")
    else:
        numbers.append(value)

print("Entered list:", numbers)
