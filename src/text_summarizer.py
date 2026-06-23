"""import nltk
nltk.download('punkt_tab')
#nltk.download('punkt')
#nltk.download('stopwords')
print("punkt_tab setup successful!")"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = """
Artificial Intelligence is transforming the world by enabling machines to perform tasks that normally require human intelligence.
It is used in healthcare, education, finance, transportation and many other industries.
AI systems can analyze large amounts of data, recognize patterns and make decisions faster than humans.
As technology advances, AI is expected to play an even greater role in improving efficiency and solving complex problems.
"""

sentences = sent_tokenize(text)

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Total Sentences:", len(sentences))
print("Total Words:", len(words))
print("Important Words:", len(filtered_words))