# Lab 6 - Deep Learning for NLP

Everything is in `Lab_06.ipynb`:

1. Load the Yelp reviews (`dataset/07-yelp-dataset.txt`), clean the text and split 80/20.
2. Task 1: tokenize the reviews, train a skip-gram Word2Vec model (200 dimensions) and turn each review into the average of its word vectors.
3. Task 2: build a feed-forward network in PyTorch (200 -> 128 -> 64 -> 32 -> 1), train it for 15 epochs with BCEWithLogitsLoss and Adam.
4. Evaluate on the test set (accuracy, classification report, confusion matrix).

The notebook is already run, so the outputs show without running anything. The accuracy is about 0.50 (the network barely learns with this little data and 15 epochs), the notes at the end explain why.

## How to run

Open `Lab_06.ipynb` in Jupyter or VS Code and run all cells.

## Libraries

- torch
- pandas
- scikit-learn
- nltk
- gensim
