count = int(input("How many elements? "))
numbers = []

for _ in range(count):
    numbers.append(int(input("Enter an element: ")))

odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)
