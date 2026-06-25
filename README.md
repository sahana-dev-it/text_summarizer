# Text Summarizer

## Overview

Text Summarizer is a Python-based Natural Language Processing (NLP) application that generates concise summaries from large blocks of text. The application uses sentence scoring and word frequency analysis to identify the most important sentences and create a meaningful summary.

The project provides a simple graphical user interface (GUI) built with Tkinter, allowing users to enter text, generate summaries, view statistics, and save summaries to a file.

## Features

* User-friendly GUI using Tkinter
* Enter and summarize large text passages
* Automatic extractive text summarization
* Clear input and output fields
* Save generated summaries to a text file
* Displays summary statistics
* Calculates compression rate
* Warning and success popup messages

## Technologies Used

* Python
* NLTK (Natural Language Toolkit)
* Tkinter
* Heapq
* Collections Module

## How It Works

1. The user enters a large text passage.
2. The application tokenizes the text into sentences and words.
3. Stopwords are removed from the text.
4. Word frequencies are calculated.
5. Sentences are scored based on important words.
6. The highest-scoring sentences are selected.
7. A summary is generated and displayed.
8. Statistics such as sentence counts and compression rate are shown.

## Statistics Displayed

The application displays:

* Original Sentences
* Summary Sentences
* Compression Rate (%)

## Example

### Input

Artificial Intelligence is one of the most important technologies today. It is used in healthcare, education, and business. AI helps doctors diagnose diseases. Businesses use AI for data analysis and decision-making. AI is expected to play a major role in the future.

### Output Summary

AI helps doctors diagnose diseases. Businesses use AI for data analysis and decision-making.

### Statistics

Original Sentences: 5

Summary Sentences: 2

Compression Rate: 60%

## Future Enhancements

* User-selectable summary length (Short, Medium, Long)
* Improved user interface design
* Export summaries in different formats
* Advanced NLP-based summarization techniques
* Dark mode support

## Author
sahana GS
BCA Student
Text Summarization Project using Python, NLTK, and Tkinter.
