n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number of terms.")
else:
    first, second = 0, 1
    print(f"The first {n} numbers in the Fibonacci series are:")

    for i in range(n):
        print(first, end=" " if i == n - 1 else ", ")
        first, second = second, first + second
    print()
