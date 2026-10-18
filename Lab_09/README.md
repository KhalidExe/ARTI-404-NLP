# Lab 9 - Named Entity Recognition (NER)

Everything is in `Lab_09.ipynb`. It has the lab examples and my answers for the tasks:

1. NER with the pre-trained spaCy model (`en_core_web_sm`): entities, labels, positions and `spacy.explain`.
2. Checking the entity alignment (BILUO tags) for custom annotations.
3. Task 1: find the entities of a sentence and print their details. I used a fixed sentence instead of `input()` so the notebook runs without typing (the `input()` line is there as a comment).
4. Task 2: find the missing entities in a contract paragraph, add them, count PERSON and ORG, and visualize them with displaCy.
5. Task 3: train a custom NER model for 20 iterations on one example, save it in `custom_ner_model`, and load it again to test it.

The visualization of the custom model was in the middle of the lab, but it needs the saved model from Task 3, so I moved it to the end.

The notebook is already run, so the outputs show without running anything. The `custom_ner_model` folder is the model saved by Task 3.

## How to run

Open `Lab_09.ipynb` in Jupyter or VS Code and run all cells. You need the spaCy model once: `python -m spacy download en_core_web_sm`.

## Libraries

- spacy (with `en_core_web_sm`)
