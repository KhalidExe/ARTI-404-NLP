# Lab 8 - Part-of-Speech (POS) Tagging

Everything is in `Lab_08.ipynb`. It has the lab examples and my answers for the tasks:

1. POS tagging with NLTK (`pos_tag`) and with spaCy (coarse `pos_` and fine-grained `tag_`).
2. Visualizing the dependency parse with displaCy.
3. Finding the adjectives in a short product review.
4. Task 1: the POS tag, the fine-grained tag and its meaning for the word "play", and the tags of all the words in the sentence.
5. Task 2: comparing the tags of "google" and "table" in different sentences.
6. Task 3: displaCy visualization of a sentence.

The notebook is already run, so the outputs show without running anything.

## How to run

Open `Lab_08.ipynb` in Jupyter or VS Code and run all cells. The first cell downloads the NLTK data, and you need the spaCy model once: `python -m spacy download en_core_web_sm`.

## Libraries

- nltk
- spacy (with `en_core_web_sm`)
