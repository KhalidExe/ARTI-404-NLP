# Lab 7 - Large Language Models (LLMs)

Everything is in `Lab_07.ipynb`:

1. Part A: text generation with a decoder-only model (DistilGPT-2).
2. Part B: French translation with an encoder-decoder model (FLAN-T5-small).
3. Part C: sentiment classification with an encoder-only model (DistilBERT).
4. Task 1: choose the model family for 5 NLP tasks.
5. Task 2: run the sentiment classifier on 3 sentences.
6. Task 3: summarize a paragraph with FLAN-T5.
7. Task 5: short reflection on why chatbots use decoder-only models.
8. Optional challenge: generate without a seed and explain why the outputs change.

The notebook is already run, so the outputs show without running anything. The sampling outputs without a seed change every time.

## How to run

Open `Lab_07.ipynb` in Jupyter or VS Code and run all cells. The first run downloads the three models from Hugging Face, so it needs internet.

## Libraries

- transformers
- sentencepiece
- torch
