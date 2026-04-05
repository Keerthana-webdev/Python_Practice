from collections import Counter

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)

    freq = Counter(words)
    most_common = freq.most_common(1)

    return word_count, char_count, most_common

text = input("Enter text: ")

wc, cc, mc = analyze_text(text)

print("Words:", wc)
print("Characters:", cc)
print("Most frequent word:", mc)