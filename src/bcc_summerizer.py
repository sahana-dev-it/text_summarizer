from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import os

# Read article

category = "tech"

folder_path = os.path.join("data", "News Articles", category)

file_name = "001.txt"

file_path = os.path.join(folder_path, file_name)

with open(file_path, "r", encoding="latin-1") as f:
    article = f.read()

# Tokenization

sentences = sent_tokenize(article)
words = word_tokenize(article)

# Stopword removal and word frequency calculation

stop_words = set(stopwords.words("english"))

word_frequencies = defaultdict(int)

for word in words:

    word = word.lower()

    if word.isalnum() and word not in stop_words:
        word_frequencies[word] += 1

# Sentence scoring

sentence_scores = defaultdict(int)

for sentence in sentences:

    sentence_words = word_tokenize(sentence.lower())

    for word in sentence_words:

        if word in word_frequencies:
            sentence_scores[sentence] += word_frequencies[word]

# Generate summary

average_score = sum(sentence_scores.values()) / len(sentence_scores)

summary = ""

for sentence in sentences:

    if sentence_scores[sentence] >= average_score:
        summary += sentence + " "

print("ORIGINAL ARTICLE:\n")
print(article[:1000])

print("\n" + "=" * 50)

print("\nSUMMARY:\n")
print(summary)