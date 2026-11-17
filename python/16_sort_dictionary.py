import operator

my_dict = {}

while True:
    key = input("Enter a key (or 'q' to quit): ")
    if key == "q":
        break

    value = int(input("Enter a value: "))
    my_dict[key] = value

print("Original dictionary:", my_dict)

ascending = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
print("Dictionary in ascending order by value:", ascending)

descending = dict(
    sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
)
print("Dictionary in descending order by value:", descending)
