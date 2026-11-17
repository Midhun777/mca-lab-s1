word_list = input("Enter a list of words (comma-separated): ").split(",")

longest_word = ""
longest_length = 0

for word in word_list:
    word = word.strip()
    current_length = len(word)

    if current_length > longest_length:
        longest_length = current_length
        longest_word = word

print(f"Longest word: {longest_word!r} with length {longest_length}")
