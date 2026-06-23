import os
path = "data/News Articles"
print("categories in dataset:")
for folder in os.listdir(path):
    print(folder)