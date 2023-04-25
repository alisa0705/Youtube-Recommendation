## Show Recommendation System
This library provides show recommendations based on the user input. 

### I. Project Overview
* Phase 1: `youtube.py` includes a python tool that connect to Youtube API to retrieve show information (title and genre) for a pre-defined set of genres. 
    * Input: 
        * Video genres provided in a list of strings format
        * The number of videos to retrieve 
    * Output: The results are saved into a csv file. 
* Phase 2: `recommend.py` includes a python tool that consumes the output csv file from the previous phase and generates video recommendations based on user-input. 
    * Input: A string describing video title or genre
    * Output: 10 recommended shows
* Phase 3: Write tests and documentation


### II. Setup Instructions
- [ ] In your local terminal, clone the repo
- [ ] Python version: `3.10 and above`
- [ ] Required library: `google-api-python-client`, `langdetect`, `nltk`, `numpy`, `pandas`, `scikit_learn`

### III. Details of Each Function/Class

### IV. Examples
```python
>> retrieve_shows(["Comedy", "Drama", "Action", "Horror", "Music", "Art"], 500) # Output is a csv file

>>> show_recommendation() # After running this line, users will see the following prompt where they are instructed to enter video information after the colon. 
Enter a video title or genre: `comedy`
                                               Title   Genre                                          URL
0                  Summer Season Niha Sisters Comedy  Comedy  https://www.youtube.com/watch?v=5W3L5c3rdow
1  Mustwatch Desi New Funny Comedy Video Funniest...  Comedy  https://www.youtube.com/watch?v=cvI4_Ezycvc
2                                             Comedy  Comedy  https://www.youtube.com/watch?v=kjThpdyUBd8
3                 Wait For Twist Shorts Funny Comedy  Comedy  https://www.youtube.com/watch?v=PvRy8iCoGu8
4              Wife Vs Husband Ytshorts Comedy Funny  Comedy  https://www.youtube.com/watch?v=ngX5sT_RaQg
5      Khmer Comedy Si Khos Short Film Haha So Funny  Comedy  https://www.youtube.com/watch?v=d8Ve75oIrpA
6            Matt Rife Only Fans Full Comedy Special  Comedy  https://www.youtube.com/watch?v=2m2520TuUdk
7  New Very Special Funny Video Must Watch Amazin...  Comedy  https://www.youtube.com/watch?v=QPC2hMWY7BA
8  Must Watch Police Wali New Comedy Video Maha F...  Comedy  https://www.youtube.com/watch?v=5crScEeQBIM
9  Father Vs Son Part Shorts Prashucomedy Nana Pr...  Comedy  https://www.youtube.com/watch?v=pgp9B3iqDPU

```

### V. Test Instruction

To run pytest and check test coverage, run the following code in terminal: 
```
pip install --upgrade pip && pip install -r requirements.txt
pytest main_test.py
coverage run -m pytest tests/test_main.py > test_report.txt
coverage report -m
```
