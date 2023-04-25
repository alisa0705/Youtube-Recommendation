
import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords') # Uncomment to download for initial run
import ipywidgets as widgets
from IPython.display import display


# Read into CSV
data = pd.read_csv("video_info.csv")
data = data.drop_duplicates(subset='Title', keep="first")

# Confirm no null and duplicate values
assert (data.isnull().sum() == 0).all(
) == True, "Please review input csv file. Null values detected."

assert data.duplicated(subset='Title').sum() == 0, "Remove duplicative values in the input csv file."

# %%
data.info()


# stemmer = nltk.SnowballStemmer("english")
stopword=set(stopwords.words('english'))

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
    # text=" ".join(text)
    # text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
data["Title"] = data["Title"].apply(clean)

clean(data['Title'][0] + ' ' + data['Genre'][0])

vectorizer = TfidfVectorizer(ngram_range=(1,2))

tfidf = vectorizer.fit_transform(data["Title"])

def search(title):
    title = clean(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = data.iloc[indices].iloc[::-1]
    
    return results


movie_input = widgets.Text(
    value='Enter Show Here',
    description='Video Title:',
    disabled=False
)
movie_list = widgets.Output()

def on_type(data):
    with movie_list:
        movie_list.clear_output()
        title = data["new"]
        if len(title) > 3:
            display(search(title))

movie_input.observe(on_type, names='value')


display(movie_input, movie_list)


