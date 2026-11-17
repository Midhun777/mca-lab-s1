dict1 = {}
dict2 = {}

print("Enter elements of the first dictionary:")
while True:
    key = input("Enter a key (or 'q' to quit): ")
    if key == "q":
        break

    value = int(input("Enter a value: "))
    dict1[key] = value

print("Enter elements of the second dictionary:")
while True:
    key = input("Enter a key (or 'q' to quit): ")
    if key == "q":
        break

    value = int(input("Enter a value: "))
    dict2[key] = value

merged_dict = dict1 | dict2
print(merged_dict)
