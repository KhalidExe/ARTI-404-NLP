# ARTI 404 - Lab 1: Intro to NLP
# Task 1: dataset type chosen = CSV (IMDB Dataset of 50K Movie Reviews)
# Task 2: download the dataset, open it and explore it

import os

import kagglehub
import nltk
import pandas as pd

print("NLTK version:", nltk.__version__)

# download the dataset from Kaggle
path = kagglehub.dataset_download("lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
print("Path to dataset files:", path)

# load the CSV into a dataframe
csv_path = os.path.join(path, "IMDB Dataset.csv")
df = pd.read_csv(csv_path)

print("\nFirst rows:")
print(df.head())

print("\nDescribe:")
print(df.describe())

print("\nInfo:")
df.info()

# check class distribution
print("\nSentiment distribution:")
print(df["sentiment"].value_counts())
