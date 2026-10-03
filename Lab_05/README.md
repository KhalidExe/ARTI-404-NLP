# Lab 5 - Text Representation

Everything is in `Lab_05.ipynb`:

1. Cosine similarity between 4 sentences (using TF-IDF vectors).
2. TF-IDF on 3 sentences to find the important words.
3. Preprocessing the Simpsons script lines (`spoken_words`) and training a skip-gram Word2Vec model with gensim.
4. `most_similar()` for homer, marge and bart.
5. `doesnt_match()` for three groups of names.

The Simpsons dataset (`dataset/simpsons_script_lines.csv`) is the one given with the lab. The notebook is already run, so the outputs show without running anything. The Word2Vec results change a little between runs.

## How to run

Open `Lab_05.ipynb` in Jupyter or VS Code and run all cells (training the model takes about a minute).

## Libraries

- pandas
- scikit-learn
- nltk
- gensim
