num_list = []

n = int(input("Enter the number of values in the list: "))
print("Enter the elements:")

for _ in range(n):
    num_list.append(int(input()))

total = 0
for item in num_list:
    total += item

print("The sum of all items in the list is:", total)
