"""
A module that recommends 5 Youtube videos based on user input.
Adopted from: https://www.youtube.com/watch?v=eyEabQRBMQA.
"""

import string
import re
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")


# Read into CSV
videos = pd.read_csv("video_info.csv")
videos = videos.drop_duplicates(subset="Title", keep="first")


# Confirm no null and duplicate values
assert (
    videos.isnull().sum() == 0
).all() == True, "Please review input csv file. Null values detected."
assert (
    videos.duplicated(subset="Title").sum() == 0
), "Remove duplicative values in the input csv file."

stopword = set(stopwords.words("english"))


def clean(text: str) -> str:
    """
    Clean show titles.

    Args:
        text (str): A string of text to be cleaned.

    Returns:
        str: The cleaned text string.
    """

    # Convert text to title case
    text = str(text).title()
    # Remove URLs
    text = re.sub("https?://\S+|www\.\S+", "", text)
    # Remove HTML tags
    text = re.sub("<.*?>+", "", text)
    # Remove punctuation marks
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    # Remove newline characters
    text = re.sub("\n", "", text)
    # Remove non-English characters
    text = re.sub("[^a-zA-Z0-9 \n\.]", "", text)
    # Remove emojis
    text = re.sub("[^\w\s,]", "", text)
    # Remove words with numbers
    text = re.sub("\w*\d\w*", "", text)
    # Remove stop words
    text = [word for word in text.split(" ") if word not in stopword]
    # Remove empty words
    text = [word for word in text if word != ""]
    # Join the remaining words
    text = " ".join(text)
    # Return the cleaned text
    return text


# Clean the "Title" column using the "clean" function and overwrite the existing column
videos["Title"] = videos["Title"].apply(clean)

# Create a TfidfVectorizer object with unigrams and bigrams
vectorizer = TfidfVectorizer(ngram_range=(1, 2))

# Fit the vectorizer to the "Genre" column of the data
# and transform the data into a TF-IDF matrix
tfidf = vectorizer.fit_transform(videos["Genre"])


def search(user_input: str) -> object:
    """
    Returns a pandas dataframe with the top 5 recommended shows based on the cosine similarity
    between the user input and the genres in the data.

    Args:
        title (str): The title of the show to use as the query.

    Returns:
        A dataframe with the columns "Title", "Genre", and "URL" for the top 5 recommended shows.
    """
    # Clean the input title
    user_input_ = clean(user_input)
    # Convert the input title to a tf-idf vector
    query_vec = vectorizer.transform([user_input_])
    # Calculate the cosine similarity between the input title and all the titles in the data
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    # Get the indices of the top 10 shows with the highest cosine similarity to the input title
    indices = np.argpartition(similarity, -5)[-5:]
    # Get the top 5 recommended shows and reverse the order
    results = videos.iloc[indices].iloc[::-1].reset_index(drop=True)
    # Return the top 5 recommended shows with the columns "Title", "Genre", and "URL"
    return results[["Title", "Genre", "URL"]]


def show_recommendation():
    """
    Prompts the user to enter a video genre and displays recommendations based on the input.
    """
    # Prompt the user to enter a video title
    user_input = input("Enter a video genre: ")
    # Display recommendations based on the input
    print(search(user_input))


if __name__ == "__main__":
    show_recommendation()
