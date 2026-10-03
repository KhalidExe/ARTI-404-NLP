# Lab 4 - Classification and Evaluation in NLP

Everything is in `Lab_04.ipynb`. It does sentiment analysis (positive, negative, neutral) on the Amazon unlocked phones reviews from Kaggle:

1. Load the data, make the labels from the star rating, and do 5 preprocessing steps (lowercase, remove HTML and links, remove punctuation and numbers, remove stop words, lemmatization).
2. Train/test split (80/20).
3. TF-IDF features.
4. Naive Bayes classifier.
5. Evaluation (accuracy and classification report) and the confusion matrix.

I used a random sample of 50,000 reviews so it runs faster. The accuracy is about 85%, but the neutral class is almost never predicted (explained at the end of the notebook).

The notebook is already run, so the outputs show without running anything.

## How to run

Open `Lab_04.ipynb` in Jupyter or VS Code and run all cells. You need internet the first time to download the dataset and the NLTK data.

## Libraries

- pandas
- nltk
- scikit-learn
- matplotlib
- kagglehub
