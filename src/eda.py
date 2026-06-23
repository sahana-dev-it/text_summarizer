import os
import pandas as pd

path = "data/News Articles"

print("Categories in dataset:")

for folder in os.listdir(path):
    print(folder)

data = []

for category in os.listdir(path):
    folder_path = os.path.join(path, category)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            data.append([category, text])

df = pd.DataFrame(data, columns=["category", "text"])

print(df.head())    