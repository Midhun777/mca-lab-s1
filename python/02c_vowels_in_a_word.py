word = input("Enter the word: ")

vowels = ["a", "e", "i", "o", "u"]
word_vowels = []

for character in word:
    if character.lower() in vowels and character.lower() not in word_vowels:
        word_vowels.append(character.lower())

print("Vowels in", word, "are:", word_vowels)
