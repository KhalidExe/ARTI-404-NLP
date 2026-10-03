# Lab 3 - N-Grams

Everything is in `Lab_03.ipynb`. It builds a bigram language model (MLE) with NLTK on a Kaggle dataset of tweets from Pakistan and uses it to:

1. Clean the tweets (remove RT, links, mentions, hashtags and emojis).
2. Train the model and generate a few tweets.
3. Evaluate it with perplexity (test perplexity is `inf` because MLE gives 0 to bigrams it never saw, explained in the notebook).
4. Get the probability of the bigram "pakistan is" and the perplexity of the word "pakistan".

The notebook is already run, so the outputs show without running anything.

## How to run

Open `Lab_03.ipynb` in Jupyter or VS Code and run all cells. You need internet the first time to download the dataset.

## Libraries

- nltk
- pandas
- kagglehub
- emoji
