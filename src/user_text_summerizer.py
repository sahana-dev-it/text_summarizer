from nltk.tokenize import sent_tokenize, word_tokenize   # Used to split text into sentences and words
from nltk.corpus import stopwords                        # Used to remove common words like 'the', 'is', 'and'
from collections import defaultdict                      # Creates a dictionary with default value 0
import heapq                                             # Used to find highest scoring sentences
import os                                                # Used to create folders and save files

print("\nTEXT SUMMARIZER")
print("-" * 30)

# Take paragraph input from the user
article = input("Paste your text: ")

# Split the paragraph into individual sentences
sentences = sent_tokenize(article)

# Split the paragraph into individual words
words = word_tokenize(article)

# Load English stop words
stop_words = set(stopwords.words("english"))

# Dictionary to store frequency of important words
word_frequencies = defaultdict(int)

# Count frequency of each important word
for word in words:

    # Convert word to lowercase so Python and python are treated the same
    word = word.lower()

    # Ignore punctuation and stop words
    if word.isalnum() and word not in stop_words:

        # Increase frequency count of the word
        word_frequencies[word] += 1

# Dictionary to store score of each sentence
sentence_scores = defaultdict(int)

# Check every sentence
for sentence in sentences:

    # Convert sentence to lowercase and split into words
    sentence_words = word_tokenize(sentence.lower())

    # Check every word in the sentence
    for word in sentence_words:

        # If the word exists in the frequency dictionary
        if word in word_frequencies:

            # Add its frequency to the sentence score
            sentence_scores[sentence] += word_frequencies[word]

# Select one-third of the total sentences for the summary
summary_length = max(1, len(sentences) // 3)

# Select the highest scoring sentences
best_sentences = heapq.nlargest(
    summary_length,
    sentence_scores,
    key=sentence_scores.get
)

# Combine selected sentences into one summary
summary = " ".join(best_sentences)

print("\nSUMMARY")
print("-" * 30)

# Display the generated summary
print(summary)

# Create folder if it does not already exist
os.makedirs("data/summaries", exist_ok=True)

# Save the summary into a text file
with open(
    "data/summaries/user_summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(summary)

# Display success message
print("\nSummary saved successfully!")