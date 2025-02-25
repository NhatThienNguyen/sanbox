"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""
from operator import itemgetter

words_to_number = {}
text = input("Text: ")
for word in text.split():
    words_to_number[word] = len(word)

max_width = max(len(word) for word in words_to_number.keys())

for word, number in sorted(words_to_number.items(), key=itemgetter(0)):
    print(f"{word:{max_width}} : {number}")