# Lab 13 - Information Retrieval for RAG

## What it does
- **Part 1 (`Lab_13_Part_1.ipynb`):** builds a small information retrieval system. It converts 6 short NLP notes into TF-IDF vectors, converts a query with the same vectorizer, ranks the documents with cosine similarity and returns the top-k. It also has the two exercises (change the query, change k).
- **Part 2 (`Lab_13_Part_2.ipynb`):** puts the steps in a `search()` function, compares sparse and dense retrieval, shows that a top result can have a score of 0, adds `search_filtered()` to skip zero scores, and has the practice questions (named entity recognition search, and adding a new document and rebuilding the TF-IDF vectors).

## How to run
1. Install the library: `pip install scikit-learn`
2. Open each notebook in VS Code or Jupyter.
3. Run all cells.

## Libraries
- scikit-learn (TfidfVectorizer, cosine_similarity)
