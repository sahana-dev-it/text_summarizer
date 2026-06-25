import os
import tkinter as tk
from tkinter import messagebox
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import heapq


def summarize_text():

    article = input_text.get("1.0", tk.END)

    if article.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter some text first!"
        )
        return

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

    compression_rate = (
        (original_sentences - summary_sentences)
        / original_sentences
    ) * 100

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

    stats_label.config(
        text=
        f"Original Sentences: {original_sentences} | "
        f"Summary Sentences: {summary_sentences} | "
        f"Compression Rate: {compression_rate:.2f}%"
    )


def clear_text():

    input_text.delete("1.0", tk.END)

    output_text.delete("1.0", tk.END)

    stats_label.config(
        text="Statistics will appear here"
    )


def save_summary():

    summary = output_text.get("1.0", tk.END)

    if summary.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please generate a summary first!"
        )
        return

    os.makedirs("data/summaries", exist_ok=True)

    with open(
        "data/summaries/user_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(summary)

    messagebox.showinfo(
        "Success",
        "Summary saved successfully!"
    )


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

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

summarize_button = tk.Button(
    button_frame,
    text="Summarize",
    command=summarize_text
)
summarize_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text
)
clear_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(
    button_frame,
    text="Save Summary",
    command=save_summary
)
save_button.pack(side=tk.LEFT, padx=10)

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

stats_label = tk.Label(
    root,
    text="Statistics will appear here",
    font=("Arial", 10)
)
stats_label.pack(pady=10)

root.mainloop()