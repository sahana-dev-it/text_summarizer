# AI Text Summarizer Project – Day 1 Notes

## Project Name

AI Text Summarizer

## Objective

To build an AI-based Text Summarizer using Python, Hugging Face Transformers, and NLP concepts.

## Work Completed

### 1. Project Setup

* Created a project folder named `text_summarizer`.
* Opened the project in VS Code.
* Initialized Git using `git init`.
* Connected the local project with GitHub repository.

### 2. Project Structure Creation

Created the following folders:

* src
* data
* docs

Purpose:

* `src` → stores source code.
* `data` → stores datasets.
* `docs` → stores project documentation.

### 3. README Creation

Created `README.md`.

Added:

* Project Name
* Student Name
* Tech Stack
* Project Description

Purpose:
README helps others understand the project.

### 4. Git and GitHub Learning

Learned:

`git add .`

* Adds files to staging area.

`git commit -m "message"`

* Creates a project checkpoint.

`git push`

* Uploads local project to GitHub.

### 5. Git Conflict Resolution

Encountered a README merge conflict while pushing.

Learned:

* Why conflicts happen.
* How to resolve conflicts manually.
* How to commit the resolved version.

### 6. Dataset Download

Downloaded BBC News Summary Dataset from Kaggle.

Dataset Structure:

* News Articles
* Summaries

Article Categories:

* business
* entertainment
* politics
* sport
* tech

### 7. Project Planning

Created `project_plan.md`.

Included:

* Problem Statement
* Objectives
* Technologies Used
* Future Enhancements

### 8. AI Environment Setup

Installed required libraries:

* transformers
* torch
* sentencepiece

Purpose:
These libraries allow us to use pretrained AI models for text summarization.

### 9. First AI Summarizer File

Created:

src/test_ai.py

Purpose:
To test whether an AI model can generate summaries successfully.

## Concepts Learned

### Git

Version control system used to track project changes.

### GitHub

Online platform used to store and share code.

### NLP (Natural Language Processing)

A field of AI that enables computers to understand and process human language.

### Transformers

Advanced AI models used for language tasks such as summarization, translation, and question answering.

### Hugging Face

A platform providing pretrained AI models that can be used without training from scratch.

## Current Project Status

Completed:

* Project Setup
* GitHub Setup
* Dataset Download
* Project Planning
* AI Library Installation

Next Step:
Run the first AI summarization program and generate the first summary using a pretrained transformer model.
## how nlk summarizes
1. Read article
2. Split into sentences
3. Split into words
4. Remove stopwords
5. Find important words
6. Score each sentence
7. Pick best sentences
8. Create summary