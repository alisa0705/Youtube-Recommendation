# Show Recommendation System
This library provides show recommendations based on the user input. 

### I. Project Overview
* Phase 1: `youtube.py` includes a python tool that connect to Youtube API to retrieve show information (title and genre) for a pre-defined set of genres. 
    * Input: 
        * Video genres provided in a list of strings format
        * The number of videos to retrieve 
    * Output: The results are saved into a csv file. 
* Phase 2: `recommend.py` includes a python tool that consumes the output csv file from the previous phase and generates video recommendations based on user-input. 
    * Input: A string describing video title or genre
    * Output: 5 show recommendation
* Phase 3: Write tests and documentation

## II. For End Users
### 1. Setup Instructions
- [ ] In your local terminal, clone the repository
- [ ] Python version: `3.10 and above`
- [ ] Required library: run `pip install --upgrade pip && pip install -r requirements.txt` to set up your environment
    * for `youtube.py` and `recommend.py`: `google-api-python-client`,  `nltk`, `numpy`, `pandas`, `scikit_learn` 
    * for `test_youtube.py` and `test_recommend.py`: `pytest`, `coverage`


### 2. Examples
```python
>> retrieve_shows(["Comedy", "Drama", "Action", "Horror"], 200) # Output is a csv file

>>> show_recommendation() # After running this line, users will see the following prompt where they are instructed to enter video information after the colon. 
Enter a video genre: `horror`
                                               Title   Genre                                          URL
0                    The Ballerina Short Horror Film  Horror  https://www.youtube.com/watch?v=sTtmpFIaFqc
1       Paranormal Tales Bodycam Horror Game Trailer  Horror  https://www.youtube.com/watch?v=m-Pimp8vuXE
2                    Smiling Woman Short Horror Film  Horror  https://www.youtube.com/watch?v=mBYGUn6Q7tQ
3  A Jadui Mask Horror Story Horrorstories Mask S...  Horror  https://www.youtube.com/watch?v=ObiUJjzL6hM
4  Filme Horror La Care S Nu Te Uii Noaptea Life ...  Horror  https://www.youtube.com/watch?v=PAXnTLvXOTU

```

## For Contributors
### 1. Test Instruction
#### a. Install python and `pytest`.
#### b. Modify the existing `recommend.py` and `youtube.py` files. Update the test functions accordingly. 
#### c. To run pytest and check test coverage, run the following code in terminal: 

```
pytest test_youtube.py test_recommend.py
coverage run -m pytest test_youtube.py test_recommend.py > test_report.txt
coverage report -m
```

