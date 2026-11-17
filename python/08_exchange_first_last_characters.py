text = input("Enter the string: ")

if len(text) < 2:
    modified_text = text
else:
    modified_text = text[-1] + text[1:-1] + text[0]

print("Modified string:", modified_text)
