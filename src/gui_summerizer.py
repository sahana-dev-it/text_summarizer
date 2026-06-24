import tkinter as tk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import heapq


def summarize_text():

    article = input_text.get("1.0", tk.END)

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

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)


root = tk.Tk()
root.title("Text Summarizer")
root.geometry("800x600")

title = tk.Label(
    root,
    text="TEXT SUMMARIZER",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

input_label = tk.Label(
    root,
    text="Enter Text:"
)
input_label.pack()

input_text = tk.Text(
    root,
    height=10,
    width=80
)
input_text.pack(pady=10)

summarize_button = tk.Button(
    root,
    text="Summarize",
    command=summarize_text
)
summarize_button.pack(pady=10)

output_label = tk.Label(
    root,
    text="Summary:"
)
output_label.pack()

output_text = tk.Text(
    root,
    height=10,
    width=80
)
output_text.pack(pady=10)

root.mainloop()