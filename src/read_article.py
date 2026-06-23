import os

category = "tech"

folder_path = os.path.join("data", "News Articles", category)

files = os.listdir(folder_path)

print("Number of articles:", len(files))

first_file = files[0]

file_path = os.path.join(folder_path, first_file)

with open(file_path, "r", encoding="latin-1") as f:
    article = f.read()

print("\nFile Name:")
print(first_file)

print("\nFirst 500 Characters:\n")
print(article[:500])