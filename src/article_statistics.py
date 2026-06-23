import os

dataset_path = "data/News Articles"

total_words = 0
article_count = 0

largest_article = 0
smallest_article = float('inf')

for category in os.listdir(dataset_path):

    category_path = os.path.join(dataset_path, category)

    if os.path.isdir(category_path):

        for file in os.listdir(category_path):

            file_path = os.path.join(category_path, file)

            with open(file_path, "r", encoding="latin-1") as f:

                text = f.read()

                words = len(text.split())

                total_words += words
                article_count += 1

                largest_article = max(largest_article, words)
                smallest_article = min(smallest_article, words)

average_words = total_words / article_count

print("Total Articles:", article_count)
print("Average Words per Article:", round(average_words))
print("Largest Article:", largest_article, "words")
print("Smallest Article:", smallest_article, "words")