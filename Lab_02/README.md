# Lab 2 - Text Pre-processing and Regular Expressions

Everything is in `Lab_02.ipynb`, one section per task:

1. Counts all hashtags in the Apple tweets dataset (Kaggle) and shows the top 10.
2. `re.compile()` to change 2021 to 2022 in a sentence.
3. `re.split()` to split a string on digits.
4. Tokenizes a sentence with spaCy and with NLTK to compare them.

The explanations are written in the notebook under each task. The notebook is already run, so the outputs show without running anything.

## How to run

Open `Lab_02.ipynb` in Jupyter or VS Code and run all cells. Install the libraries first (the notebook lists the pip command). The first code cell downloads the spaCy model and NLTK data if they are missing, so you need internet.

## Libraries

- re, collections (built in)
- pandas
- kagglehub
- nltk
- spacy
