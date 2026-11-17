list1 = []
list2 = []

m = int(input("Enter the limit of List 1: "))
print("Enter the elements:")
for _ in range(m):
    list1.append(int(input()))

n = int(input("Enter the limit of List 2: "))
print("Enter the elements:")
for _ in range(n):
    list2.append(int(input()))

print(list1, list2)

if len(list1) == len(list2):
    print("Both lists are of the same length.")
else:
    print("Both lists are not of the same length.")

if sum(list1) == sum(list2):
    print("The sums of both lists are the same.")
else:
    print("The sums of both lists are not the same.")

common_items = [item for item in list1 if item in list2]
print("Same members are:", common_items)
