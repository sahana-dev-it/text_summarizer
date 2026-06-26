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

    selected_length = summary_option.get()

    if selected_length == "Short":
        summary_length = max(1, len(sentences) // 8)

    elif selected_length == "Long":
        summary_length = max(1, len(sentences) // 2)

    else:
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

    output_text.config(state="normal")

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

    output_text.config(state="disabled")

    stats_label.config(
        text=
        f"Original Sentences: {original_sentences} | "
        f"Summary Sentences: {summary_sentences} | "
        f"Compression Rate: {compression_rate:.2f}%"
    )


def clear_text():

    input_text.delete("1.0", tk.END)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")

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
root.geometry("1000x850")
root.configure(bg="#f0f4f7")

title = tk.Label(
    root,
    text="NLP TEXT SUMMARIZER",
    font=("Arial", 22, "bold"),
    bg="#f0f4f7",
    fg="navy"
)
title.pack(pady=10)

input_frame = tk.LabelFrame(
    root,
    text="Enter Text",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)
input_frame.pack(padx=20, pady=10, fill="both")

input_text = tk.Text(
    input_frame,
    height=12,
    width=100,
    font=("Arial", 10)
)
input_text.pack()

length_label = tk.Label(
    root,
    text="Select Summary Length:",
    bg="#f0f4f7",
    font=("Arial", 11, "bold")
)
length_label.pack()

summary_option = tk.StringVar()
summary_option.set("Medium")

short_radio = tk.Radiobutton(
    root,
    text="Short",
    variable=summary_option,
    value="Short"
)
short_radio.pack()

medium_radio = tk.Radiobutton(
    root,
    text="Medium",
    variable=summary_option,
    value="Medium"
)
medium_radio.pack()

long_radio = tk.Radiobutton(
    root,
    text="Long",
    variable=summary_option,
    value="Long"
)
long_radio.pack()

button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

summarize_button = tk.Button(
    button_frame,
    text="Summarize",
    command=summarize_text,
    width=15
)
summarize_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=15
)
clear_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(
    button_frame,
    text="Save Summary",
    command=save_summary,
    width=15
)
save_button.pack(side=tk.LEFT, padx=10)

output_frame = tk.LabelFrame(
    root,
    text="Generated Summary",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)
output_frame.pack(padx=20, pady=10, fill="both")

output_text = tk.Text(
    output_frame,
    height=12,
    width=100,
    font=("Arial", 10)
)
output_text.pack()

root.mainloop()