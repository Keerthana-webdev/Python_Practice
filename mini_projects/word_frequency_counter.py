text = input("Enter sentence: ").split()

freq = {}

for word in text:
    freq[word] = freq.get(word, 0) + 1

print(freq)