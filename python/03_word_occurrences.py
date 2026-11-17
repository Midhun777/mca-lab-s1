sentence = input("Enter the sentence: ")
words = sentence.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
