# Lab 11 - Attention with RNN

## What it does
- Loads a small question and answer dataset (168 questions, 12 answer groups) from the `dataset` folder.
- Preprocesses the questions (lowercase, tokenization, padding).
- Builds an RNN in PyTorch with an attention layer and trains it to choose the right answer group.
- Shows the attention weights as bar charts.
- Task 1: attention bar charts for three different questions, with the highest attention word of each.
- Task 2: compares the attention of two questions that have a similar meaning.

## How to run
1. Install the libraries: `pip install torch tensorflow pandas matplotlib`
2. Open `Lab_11.ipynb` in VS Code or Jupyter (keep the `dataset` folder next to it).
3. Run all cells.

## Libraries
- torch
- tensorflow (only for the Keras Tokenizer and pad_sequences)
- pandas
- matplotlib
