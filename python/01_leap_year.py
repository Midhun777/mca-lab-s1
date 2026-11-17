current_year = int(input("Enter the current year: "))
future_year = int(input("Enter the future year: "))

print("Leap years:")

for year in range(current_year, future_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year)
