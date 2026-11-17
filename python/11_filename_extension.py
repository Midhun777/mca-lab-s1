filename = input("Enter the filename: ")

file_parts = filename.rsplit(".", 1)
extension = file_parts[-1] if len(file_parts) == 2 else ""

print("File extension is:", extension)
