# Lab 12 - Transformers

## What it does
- Loads DistilBERT (fine-tuned for sentiment) with Hugging Face Transformers and prints its layers, heads and hidden size.
- Tokenizes a sentence and shows the tokens.
- Shows the embeddings and the self-attention weights.
- Classifies the sentence as positive or negative with a softmax.
- Task: loads `bert-base-uncased`, prints the number of layers and heads, the total number of attention heads, and the attention weights of the third layer and second head for a sentence, then explains the rows and columns of the matrix.

## How to run
1. Install the libraries: `pip install transformers torch matplotlib pandas`
2. Open `Lab_12.ipynb` in VS Code or Jupyter.
3. Run all cells (the models are downloaded the first time, so internet is needed).

## Libraries
- transformers
- torch
- pandas
- matplotlib
