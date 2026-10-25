# Lab 10 - Introduction to Machine Translation

## What it does
- Explains the idea of neural machine translation (encoder-decoder).
- Builds a small English to French translation model with Keras (Embedding, LSTM encoder, RepeatVector, LSTM decoder, softmax).
- Task 1: answers the questions about the Embedding layer, Encoder LSTM, Decoder LSTM and softmax.
- Task 2: trains the same kind of model on the Kaggle English-French dataset (short sentences, 10,000 pairs) and tests it on some sentences.

## How to run
1. Install the libraries (the first cell in the notebook does this).
2. Open `Lab_10.ipynb` in VS Code or Jupyter.
3. Run all cells. The dataset is downloaded automatically with `kagglehub`.

## Libraries
- tensorflow
- numpy
- pandas
- scikit-learn
- kagglehub
