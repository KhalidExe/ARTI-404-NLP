# ARTI 404 - Lab 2: Text Pre-processing and Regular Expressions

import glob
import os
import re
from collections import Counter

import kagglehub
import nltk
import pandas as pd
import spacy

# punkt data is needed for nltk tokenizers (punkt_tab on newer nltk versions)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


# ---------------------------------------------------------------
# Task 1: hashtags in the Apple tweets dataset
# ---------------------------------------------------------------
print("=" * 50)
print("Task 1: Hashtags")
print("=" * 50)

path = kagglehub.dataset_download("seriousran/appletwittersentimenttexts")
csv_file = glob.glob(os.path.join(path, "*.csv"))[0]
df = pd.read_csv(csv_file)
# the tweets are in the "text" column (fall back to the first column if not)
text_col = "text" if "text" in df.columns else df.columns[0]
print("Loaded:", os.path.basename(csv_file), "| shape:", df.shape)

# hashtag = # followed by letters/digits/underscore
hashtag_pattern = re.compile(r"#\w+")

all_hashtags = []
for tweet in df[text_col].dropna():
    # lowercase so #Apple and #apple count as the same hashtag
    all_hashtags.extend(h.lower() for h in hashtag_pattern.findall(str(tweet)))

print("Total hashtags:", len(all_hashtags))
print("Unique hashtags:", len(set(all_hashtags)))
print("Top 10 hashtags:")
for tag, count in Counter(all_hashtags).most_common(10):
    print(f"  {tag}: {count}")


# ---------------------------------------------------------------
# Task 2: re.compile()
# ---------------------------------------------------------------
print("\n" + "=" * 50)
print("Task 2: re.compile()")
print("=" * 50)

text = "This year is 2021"
digits = re.compile(r"\d+")  # one or more digits

print("Type of compiled pattern:", type(digits))
new_text = digits.sub("2022", text)
print("Updated text:", new_text)

# re.compile() turns the regex string into a pattern object once, so we can
# reuse it (search, sub, findall...) without re-parsing it every time. It also
# keeps the code cleaner when the same pattern is used in many places.


# ---------------------------------------------------------------
# Task 3: re.split()
# ---------------------------------------------------------------
print("\n" + "=" * 50)
print("Task 3: re.split()")
print("=" * 50)

text = "a 11 b 2 3 c 4"
parts = re.split(r"\d+", text)
print("Result:", parts)

# re.split() cuts the string at every place the pattern matches and returns
# the pieces as a list. Unlike str.split() the separator can be a regex.


# ---------------------------------------------------------------
# Task 4: Tokenization with spaCy vs NLTK
# ---------------------------------------------------------------
print("\n" + "=" * 50)
print("Task 4: spaCy vs NLTK tokenization")
print("=" * 50)

text = "I'm enjoying the NLP course!"

# spacy.load() loads a trained pipeline (here the small English model) from
# disk and returns an nlp object with a tokenizer, tagger, parser, etc.
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("spaCy tokens:")
for token in doc:
    print(token.text)

print("\nNLTK tokens:")
print(nltk.word_tokenize(text))

# Differences: on this sentence both tokenizers split "I'm" into "I" and "'m"
# and take "!" as its own token, so the lists look the same. The difference is
# the output type: NLTK gives plain strings, while spaCy gives Token objects
# that also have attributes (lemma_, pos_, is_stop...). NLTK also needs the
# punkt data downloaded first, spaCy needs the model.
