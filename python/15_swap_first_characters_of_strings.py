string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1 and string2:
    combined = string2[0] + string1[1:] + " " + string1[0] + string2[1:]
else:
    combined = string2 + " " + string1

print(combined)
