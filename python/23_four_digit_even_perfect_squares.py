result = []

start = int(input("Enter the starting range (four-digit number): "))
end = int(input("Enter the ending range (four-digit number): "))

if start < 1000 or end > 9999 or start > end:
    print("Invalid range. Please enter a valid four-digit range.")
else:
    for number in range(start, end + 1):
        digits_are_even = all(int(digit) % 2 == 0 for digit in str(number))

        if digits_are_even:
            root = int(number ** 0.5)
            if root * root == number:
                result.append(number)

    print("Four-digit even perfect square numbers in the given range:")
    print(result)
