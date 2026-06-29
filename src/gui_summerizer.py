import os                                  # Used to create folders and save files
import tkinter as tk                       # Used to create GUI
from tkinter import messagebox             # Used to display pop-up messages
from nltk.tokenize import sent_tokenize, word_tokenize   # Used to split text into sentences and words
from nltk.corpus import stopwords          # Used to remove common words
from collections import defaultdict        # Dictionary with default value 0
import heapq                               # Used to select highest scoring sentences


# Function to generate summary
def summarize_text():

    # Read text entered by the user from the input text box
    article = input_text.get("1.0", tk.END)

    # Check if the input box is empty
    if article.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter some text first!"
        )
        return

    # Split paragraph into sentences
    sentences = sent_tokenize(article)

    # Split paragraph into words
    words = word_tokenize(article)

    # Load English stop words
    stop_words = set(stopwords.words("english"))

    # Dictionary to store frequency of important words
    word_frequencies = defaultdict(int)

    # Count frequency of important words
    for word in words:

        # Convert every word to lowercase
        word = word.lower()

        # Ignore punctuation and stop words
        if word.isalnum() and word not in stop_words:

            # Increase frequency count
            word_frequencies[word] += 1

    # Dictionary to store sentence scores
    sentence_scores = defaultdict(int)

    # Calculate score for every sentence
    for sentence in sentences:

        # Convert sentence to lowercase and split into words
        sentence_words = word_tokenize(sentence.lower())

        # Check every word in the sentence
        for word in sentence_words:

            # Add word frequency to sentence score
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]

    # Read summary length selected by the user
    selected_length = summary_option.get()

    # Decide how many sentences to include in summary
    if selected_length == "Short":
        summary_length = max(1, len(sentences) // 8)

    elif selected_length == "Long":
        summary_length = max(1, len(sentences) // 2)

    else:
        summary_length = max(1, len(sentences) // 3)

    # Select highest scoring sentences
    best_sentences = heapq.nlargest(
        summary_length,
        sentence_scores,
        key=sentence_scores.get
    )

    # Combine selected sentences into one paragraph
    summary = " ".join(best_sentences)

    # Count original and summarized sentences
    original_sentences = len(sentences)
    summary_sentences = len(best_sentences)

    # Calculate compression percentage
    compression_rate = (
        (original_sentences - summary_sentences)
        / original_sentences
    ) * 100

    # Enable output box for editing
    output_text.config(state="normal")

    # Remove previous summary
    output_text.delete("1.0", tk.END)

    # Display new summary
    output_text.insert(tk.END, summary)

    # Disable editing of output box
    output_text.config(state="disabled")

    # Display summary statistics
    stats_label.config(
        text=
        f"Original Sentences: {original_sentences} | "
        f"Summary Sentences: {summary_sentences} | "
        f"Compression Rate: {compression_rate:.2f}%"
    )


# Function to clear input and output boxes
def clear_text():

    # Clear input text
    input_text.delete("1.0", tk.END)

    # Enable output box
    output_text.config(state="normal")

    # Clear output text
    output_text.delete("1.0", tk.END)

    # Disable output box again
    output_text.config(state="disabled")

    # Reset statistics label
    stats_label.config(
        text="Statistics will appear here"
    )


# Function to save summary into a text file
def save_summary():

    # Read generated summary
    summary = output_text.get("1.0", tk.END)

    # Check whether summary exists
    if summary.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please generate a summary first!"
        )
        return

    # Create folder if it does not exist
    os.makedirs("data/summaries", exist_ok=True)

    # Save summary into a text file
    with open(
        "data/summaries/user_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(summary)

    # Show success message
    messagebox.showinfo(
        "Success",
        "Summary saved successfully!"
    )


# Create main application window
root = tk.Tk()

# Set window title
root.title("Text Summarizer")

# Set window size
root.geometry("1000x850")

# Set background color
root.configure(bg="#f0f4f7")

# Create title label
title = tk.Label(
    root,
    text="NLP TEXT SUMMARIZER",
    font=("Arial", 22, "bold"),
    bg="#f0f4f7",
    fg="navy"
)
title.pack(pady=10)

# Create frame for input text
input_frame = tk.LabelFrame(
    root,
    text="Enter Text",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)
input_frame.pack(padx=20, pady=10, fill="both")

# Create input text area
input_text = tk.Text(
    input_frame,
    height=12,
    width=100,
    font=("Arial", 10)
)
input_text.pack()

# Label for summary length options
length_label = tk.Label(
    root,
    text="Select Summary Length:",
    bg="#f0f4f7",
    font=("Arial", 11, "bold")
)
length_label.pack()

# Variable to store selected summary length
summary_option = tk.StringVar()

# Set Medium as default
summary_option.set("Medium")

# Radio button for Short summary
short_radio = tk.Radiobutton(
    root,
    text="Short",
    variable=summary_option,
    value="Short"
)
short_radio.pack()

# Radio button for Medium summary
medium_radio = tk.Radiobutton(
    root,
    text="Medium",
    variable=summary_option,
    value="Medium"
)
medium_radio.pack()

# Radio button for Long summary
long_radio = tk.Radiobutton(
    root,
    text="Long",
    variable=summary_option,
    value="Long"
)
long_radio.pack()

# Frame to hold buttons
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

# Button to generate summary
summarize_button = tk.Button(
    button_frame,
    text="Summarize",
    command=summarize_text,
    width=15
)
summarize_button.pack(side=tk.LEFT, padx=10)

# Button to clear text
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=15
)
clear_button.pack(side=tk.LEFT, padx=10)

# Button to save summary
save_button = tk.Button(
    button_frame,
    text="Save Summary",
    command=save_summary,
    width=15
)
save_button.pack(side=tk.LEFT, padx=10)

# Frame to display generated summary
output_frame = tk.LabelFrame(
    root,
    text="Generated Summary",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)
output_frame.pack(padx=20, pady=10, fill="both")

# Output text box
output_text = tk.Text(
    output_frame,
    height=12,
    width=100,
    font=("Arial", 10)
)
output_text.pack()

# Start the GUI application
root.mainloop()