from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import heapq
import os
print("\nAvailable Categories:")
print("1. business")
print("2. entertainment")
print("3. politics")
print("4. sport")
print("5. tech")
print()
category = input("Enter category : ")

folder_path = os.path.join("data", "News Articles", category)

file_name = input("Enter article file name (example: 001.txt): ")

file_path = os.path.join(folder_path, file_name)

try:
    with open(file_path, "r", encoding="latin-1") as f:
        article = f.read()

except FileNotFoundError:
    print("Error: File not found.")
    exit()
sentences = sent_tokenize(article)
words = word_tokenize(article)

stop_words = set(stopwords.words("english"))

word_frequencies = defaultdict(int)

for word in words:
    word = word.lower()

    if word.isalnum() and word not in stop_words:
        word_frequencies[word] += 1

sentence_scores = defaultdict(int)

for sentence in sentences:

    sentence_words = word_tokenize(sentence.lower())

    for word in sentence_words:

        if word in word_frequencies:
            sentence_scores[sentence] += word_frequencies[word]

summary_length = max(1, len(sentences) // 3)

best_sentences = heapq.nlargest(
    summary_length,
    sentence_scores,
    key=sentence_scores.get
)

summary = " ".join(best_sentences)

original_sentences = len(sentences)
summary_sentences = len(best_sentences)

compression = (
    (original_sentences - summary_sentences)
    / original_sentences
) * 100

print("\nSUMMARY STATISTICS")
print("-------------------")
print("Original Sentences:", original_sentences)
print("Summary Sentences:", summary_sentences)
print("Compression Rate:", round(compression, 2), "%")

os.makedirs("data/summaries", exist_ok=True)

summary_file = os.path.join(
    "data",
    "summaries",
    f"summary_{file_name}"
)

with open(summary_file, "w", encoding="utf-8") as f:
    f.write(summary)

print("\nSummary saved to:")
print(summary_file)