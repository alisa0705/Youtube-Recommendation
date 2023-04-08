## Show Recommendation System
This library provides show recommendations based on the user-specified genre. 

### I. Project Plan
* Phase 1: Connect to Youtube API to retrieve show information (title and genre) for a pre-defined set of genres. The results are saved into a csv file. 
* Phase 2: Build a recommendation system that takes a csv file as input. Define a function to clean the show information remove any unwanted characters. Define a function to recommend top 10 shows using TF-IDF and cosine similarity based on a user-input show genre.
    * Use type hints
    * Doc strings
    * Try organizing into a class
* Phase 3: Write tests and documentation


### II. Setup Instructions
- [ ] In your local terminal, clone the repo
- [ ] Python version: `3.10 and above`
- [ ] Required library: 

pandas, numpy
google-auth and google-auth-oauthlib - for authentication when connecting to the Youtube API.
google-api-python-client - for accessing the Youtube API and retrieving show information.


### III. Details of Each Function/Class

### IV. Examples
```python
>> abc
```

### V. Test Instruction

To run pytest and check test coverage, run the following code in terminal: 
```
pip install --upgrade pip && pip install -r requirements.txt
pytest main_test.py
coverage run -m pytest tests/test_main.py > test_report.txt
coverage report -m
```
