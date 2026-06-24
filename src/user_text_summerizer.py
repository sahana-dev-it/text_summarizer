from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import heapq
import os

print("\nTEXT SUMMARIZER")
print("-" * 30)

article = input("Paste your text: ")

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

print("\nSUMMARY")
print("-" * 30)
print(summary)

os.makedirs("data/summaries", exist_ok=True)

with open(
    "data/summaries/user_summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(summary)

print("\nSummary saved successfully!")