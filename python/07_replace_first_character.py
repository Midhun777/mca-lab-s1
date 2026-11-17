text = input("Enter the string: ")

first = text[0]
modified_text = first + text[1:].replace(first, "$")

print("Modified string:", modified_text)
