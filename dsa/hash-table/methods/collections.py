from collections import defaultdict

word_counts = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "apple"]:
    word_counts[word] += 1

print(dict(word_counts))