word = input("Enter the word: ")

print("Ordinal values of", word, "are:")

for character in word:
    print(character, ":", ord(character))
