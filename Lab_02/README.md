# Lab 2 - Text Pre-processing and Regular Expressions

Everything for the lab is in `main.py`, one section per task:

1. Counts all hashtags in the Apple tweets dataset (Kaggle) and prints the top 10.
2. `re.compile()` to change 2021 to 2022 in a sentence.
3. `re.split()` to split a string on digits.
4. Tokenizes a sentence with spaCy and with NLTK so you can compare them.

The short explanations for each task are written as comments in the code.

## How to run

```
pip install nltk spacy pandas kagglehub
python -m spacy download en_core_web_sm
python main.py
```

Needs internet the first time (Kaggle dataset and NLTK data download).

## Libraries

- re, collections (built in)
- pandas
- kagglehub
- nltk
- spacy
