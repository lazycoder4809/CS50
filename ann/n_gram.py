from nltk.util import ngrams
from collections import Counter

with open("sherlok.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

bigram_counts = Counter(ngrams(words, 3))



print(bigram_counts.most_common(10))
