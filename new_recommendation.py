import pandas as pd
import re
import string
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ipywidgets as widgets
from IPython.display import display

data = pd.read_csv("video_info.csv")
data = data.drop_duplicates(subset='Title', keep="first")

# Confirm no null and duplicate values
assert (data.isnull().sum() == 0).all() == True, "Please review input csv file. Null values detected."
assert data.duplicated(subset='Title').sum() == 0, "Remove duplicative values in the input csv file."

stopword = set(stopwords.words('english'))

def clean(text):
    "Clean show titles."
    text = str(text).title()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = [word for word in text if word != '']
    text = " ".join(text)
    return text

data["Title"] = data["Title"].apply(clean)
data["title_n_genre"] = data["Title"] + " " + data["Genre"]

vectorizer = TfidfVectorizer(ngram_range=(1, 3))
tfidf = vectorizer.fit_transform(data["title_n_genre"])

# def search(title):
#     title = clean(title)
#     query_vec = vectorizer.transform([title])
#     similarity = cosine_similarity(query_vec, tfidf).flatten()
#     indices = np.argpartition(similarity, -10)[-10:]
#     results = data.iloc[indices].iloc[::-1].reset_index(drop=True)

#     return results[['Title', 'Genre', 'URL']]

def search(title):
    title = clean(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()

    # Find similar words to the input title using Word2Vec model
    try:
        similar_words = w2v_model.wv.most_similar(title, topn=5)
        similar_titles = [word[0] for word in similar_words]
        similar_titles.append(title)  # Include the original title
    except KeyError:
        # Find similar words to the input title by searching the vocabulary
        similar_titles = [word for word in w2v_model.wv.index_to_key if title.lower() in word.lower()]
        similar_titles = similar_titles[:5] + [title]  # Limit to 5 similar titles plus the original title

    # Calculate cosine similarity for each similar title
    similar_scores = []
    for similar_title in similar_titles:
        query_vec = vectorizer.transform([similar_title])
        similarity = cosine_similarity(query_vec, tfidf).flatten()
        similar_scores.append(similarity)

    # Combine the scores and sort by similarity
    combined_scores = np.sum(similar_scores, axis=0)
    indices = np.argpartition(combined_scores, -10)[-10:]
    results = data.iloc[indices].iloc[::-1].reset_index(drop=True)

    return results[['Title', 'Genre', 'URL']]

# Rest of the code remains the same


movie_input = widgets.Text(
    value='Enter Here',
    description='Video Title:',
    disabled=False
)
movie_list = widgets.Output()

def on_type(data):
    with movie_list:
        movie_list.clear_output()
        title = data["new"]
        display(search(title))

movie_input.observe(on_type, names='value')

display(movie_input, movie_list)