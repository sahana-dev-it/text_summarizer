# Text Summarizer Project - Day 2 Notes

## Date

Day 2

## Objective

To explore the BBC News Summary dataset and learn the basic NLP preprocessing steps required for building a Text Summarizer.

---

## 1. Dataset Exploration

Created the file:

```text
src/explore_dataset.py
```

### Tasks Performed

* Loaded the BBC News dataset.
* Identified all available categories.
* Counted the number of articles in each category.
* Calculated the total number of articles.

### Output

Business: 510 articles

Entertainment: 386 articles

Politics: 417 articles

Sport: 511 articles

Tech: 401 articles

Total Articles: 2225

### Insights

1. Sport category contains the highest number of articles (511).
2. Business category is almost equal to Sport (510).
3. Entertainment category contains the fewest articles (386).

---

## 2. Article Statistics Analysis

Created the file:

```text
src/article_statistics.py
```

### Tasks Performed

* Read all article files from the dataset.
* Counted words in each article.
* Calculated average article length.
* Identified largest article.
* Identified smallest article.

### Results

Total Articles: 2225

Average Words per Article: 384

Largest Article: 4432 words

Smallest Article: 89 words

### Understanding

* Average article size is suitable for text summarization.
* Large articles will benefit most from summarization.
* Very short articles may not require summarization.

---

## 3. NLTK Setup

Created the file:

```text
src/text_summarizer.py
```

### Installed Resources

* punkt
* stopwords

### Purpose

These resources are required for:

* Sentence Tokenization
* Word Tokenization
* Stopword Removal

---

## 4. NLP Preprocessing

### Sentence Tokenization

Converted a paragraph into individual sentences.

Example:

Sentence 1

Sentence 2

Sentence 3

Sentence 4

Output:

Total Sentences: 4

---

### Word Tokenization

Converted text into individual words.

Output:

Total Words: 73

---

### Stopword Removal

Removed common words such as:

* the
* is
* are
* am
* of
* in

Output:

Important Words: 53

### Result

Original Words: 73

Important Words: 53

Stopwords Removed Successfully.

---

## 5. AI Text Summarizer Attempt

### Libraries Installed

* transformers
* torch
* sentencepiece

### Issue Found

The Hugging Face summarization pipeline was not available because of compatibility issues with Python 3.13.

### Decision

Continue with NLTK-based Text Summarizer first and upgrade to AI-based summarization later.

---

## Concepts Learned Today

1. Dataset Exploration
2. Article Statistics
3. NLP Basics
4. Sentence Tokenization
5. Word Tokenization
6. Stopword Removal
7. Dataset Insights
8. Project Structure
9. GitHub Workflow
10. Text Summarization Pipeline

---

## Current Project Progress

Completed:

* Project Setup
* GitHub Integration
* Dataset Download
* Dataset Exploration
* Article Statistics
* NLTK Setup
* NLP Preprocessing

Pending:

* Word Frequency Calculation
* Sentence Scoring
* Summary Generation
* Testing
* Error Handling
* Final Documentation

---

## Plan for Day 3

1. Calculate word frequencies.
2. Implement sentence scoring.
3. Select important sentences.
4. Generate the first summary.
5. Test summarizer on BBC news articles.
6. Commit progress to GitHub.

Project Status: In Progress
Estimated Completion: 35-40%
