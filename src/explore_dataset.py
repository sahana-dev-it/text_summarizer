import os

dataset_path = "data/News Articles"

total_articles = 0

print("Categories in Dataset:\n")

for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)

    if os.path.isdir(category_path):
        article_count = len(os.listdir(category_path))

        print(f"{category}: {article_count} articles")

        total_articles += article_count

print("\nTotal Articles:", total_articles)