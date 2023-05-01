# Show Recommendation System

[![checks](https://github.com/biostat821-2023/Show_Recommendation_System/actions/workflows/checks.yml/badge.svg)](https://github.com/biostat821-2023/Show_Recommendation_System/actions/workflows/checks.yml)

This command line tool provides show recommendations based on the user input. 

### I. Project Overview
* Phase 1: `youtube.py` includes a python command line tool that connect to Youtube API to retrieve show information (title and genre) for a pre-defined set of genres. 

* Phase 2: `recommend.py` includes a python command line tool that uses the output csv file from the previous phase and generates video recommendations based on user-input. It returns top 5 recommended shows based on the cosine similarity between the user input and the genres in the data.

* Phase 3: Write tests and documentation.

## II. For End Users
### 1. Setup Instructions
#### a. In your local terminal, clone the repository
#### b. Python version: `3.10 and above`
#### c. Required library: run `pip install --upgrade pip && pip install -r requirements.txt` to set up your environment
   * for `youtube.py` and `recommend.py`: `google-api-python-client`,  `nltk`, `numpy`, `pandas`, `scikit_learn`, `click`
   * for `test_youtube.py` and `test_recommend.py`: `pytest`, `coverage`

#### d. API Keys Instruction: as the video information is obtained from YouTube via API, it's important to generate your own API keys in order to run the `youtube.py` file successfully.
* Generate New API keys: follow [the instruction](https://developers.google.com/youtube/v3/getting-started) to generate a new API key. It is important to note that YouTube API has a default quota limit per day. Once this limit is exceeded, you will receive an error and will not be able to make any requests. In this case, you may consider generating a new API key.

* Store API Key in GitHub Secrets: under the repository, select `Settings` -> `Secrets and variables` -> `Codespaces`, You will see a list of secrets. You can update your new secret here. 

![5081682868404_ pic](https://user-images.githubusercontent.com/89174034/235361548-5a027165-7411-43e1-9f96-d765f899547c.jpg)

* Update Secret Name in `youtube.py` accordingly

<img width="579" alt="Screenshot 2023-05-01 at 12 23 26 PM" src="https://user-images.githubusercontent.com/105904149/235487107-ca53f546-72f9-47ef-97ec-f5c2f9a45532.png">

### 3. Input File Format
#### a. `youtube.py`:

`retrieve_shows(genres: list[str], num_show: int) -> None`

Enter the desired genres in a list of strings format and number of shows. The output is a csv file with show Title, Genre and URL. 

#### b. `recommend.py`:

`clean(text: str) -> str`

This function takes a string as input and returns the cleaned string. It remove non-English characters, emoji, numbers, whitespace, and other special characters. 

`search(_user_input: str, _data_frame: pd.DataFrame) -> pd.DataFrame`

The search function takes two parameters: _user_input and _data_frame. _user_input is a string with user's search query. _data_frame is a Pandas DataFrame that contains information about the TV shows.

It returns a dataframe that contains the TV shows that match the search query.

`show_recommendation(input_file: str) -> None`

The show recommendation takes a string representing the input file name and triggers a prompt in the terminal for users to input their genres of interest. 

It returns nothing. Instead, it prints video recommendations in the terminal. 

### 4. Examples

To generate a `.csv` file containing show information, run this line in terminal:

```python
>>> python youtube.py -g Comedy -g Drama -g Action -g Horror -n 200 videos.csv
```

To generate video recommendations, run this line in terminal: 

```python
>>> python recommend.py videos.csv
Enter a video genre: `horror`
                                               Title   Genre                                          URL
0                    The Ballerina Short Horror Film  Horror  https://www.youtube.com/watch?v=sTtmpFIaFqc
1       Paranormal Tales Bodycam Horror Game Trailer  Horror  https://www.youtube.com/watch?v=m-Pimp8vuXE
2                    Smiling Woman Short Horror Film  Horror  https://www.youtube.com/watch?v=mBYGUn6Q7tQ
3  A Jadui Mask Horror Story Horrorstories Mask S...  Horror  https://www.youtube.com/watch?v=ObiUJjzL6hM
4  Filme Horror La Care S Nu Te Uii Noaptea Life ...  Horror  https://www.youtube.com/watch?v=PAXnTLvXOTU

```

## III. For Contributors
### 1. Test Instruction
#### a. Modify the existing `recommend.py` and `youtube.py` files. Update the test functions accordingly. 
#### b. To run pytest and check test coverage, run the following code in terminal: 

```python
pytest test_youtube.py test_recommend.py
coverage run -m pytest test_youtube.py test_recommend.py > test_report.txt
coverage report -m
```

Current Coverage: 

<img width="378" alt="Screenshot 2023-05-01 at 12 21 02 PM" src="https://user-images.githubusercontent.com/105904149/235486862-50c8d780-c9c9-4d25-a058-3504b0a98cab.png">

### 2. API Keys Instruction
Follow the instruction under `II. For End Users` -> `1d. API Keys Instruction` section. 
