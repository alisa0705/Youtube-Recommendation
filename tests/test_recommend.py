""" Unit tests for recommend.py """
import pandas as pd  # type: ignore
from recommend import clean, search  # type: ignore


def test_clean():
    """Test clean function"""
    input_text = "The quick brown fox jumps over the lazy dog! 🦊🐶"
    expected = "Quick Brown Fox Jumps Lazy Dog"
    assert clean(input_text) == expected
    assert clean("Hello world") == "Hello World"
    assert clean("https://www.example.com") == ""
    assert clean("<div>Hello World</div>") == "Hello World"
    assert clean("Hello! World?") == "Hello World"
    assert clean("Stop words should be removed") == "Stop Words Removed"
    assert clean("Words with numbers 123") == "Words Numbers"
    assert clean("   ") == ""


def test_search():
    """Test search function"""
    videos = pd.DataFrame(
        {
            "Title": [
                "Harry Potter and the Philosopher’s Stone",
                "Harry Potter and the Chamber of Secrets",
                "Harry Potter and the Prisoner of Azkaban",
                "Harry Potter and the Goblet of Fire",
                "Harry Potter and the Order of the Phoenix",
                "The Hunger Games",
                "The Paddington 1",
                "The Paddington 2",
                "PBS Mystery",
            ],
            "Genre": [
                "Fantasy",
                "Fantasy",
                "Fantasy",
                "Fantasy",
                "Fantasy",
                "Action",
                "Adventure",
                "Adventure",
                "Mystery",
            ],
            "URL": [
                "https://www.youtube.com/watch?v=k4j_Uw5Ot6o",
                "https://www.youtube.com/watch?v=2E7jjf6NLy0",
                "https://www.youtube.com/watch?v=2obsq0Dc7mc",
                "https://www.youtube.com/watch?v=_JLwfq2WBO0",
                "https://www.youtube.com/watch?v=VgiM5ISPdhU",
                "https://www.youtube.com/watch?v=PbA63a7H0bo",
                "https://www.youtube.com/watch?v=zMBlAFXHX_g",
                "https://www.youtube.com/watch?v=Dx1D-YuvW8E",
                "https://www.youtube.com/watch?v=oCpg4HQNe4k&\
                    list=PLAEBaq4wDf6ZpoQc_8F0cdsIJYy-JA4HV",
            ],
        }
    )
    user_input = "fantasy"

    expected = pd.DataFrame(
        {
            "Title": [
                "Harry Potter and the Order of the Phoenix",
                "Harry Potter and the Prisoner of Azkaban",
                "Harry Potter and the Goblet of Fire",
                "Harry Potter and the Chamber of Secrets",
                "Harry Potter and the Philosopher’s Stone",
            ],
            "Genre": ["Fantasy", "Fantasy", "Fantasy", "Fantasy", "Fantasy"],
            "URL": [
                "https://www.youtube.com/watch?v=VgiM5ISPdhU",
                "https://www.youtube.com/watch?v=2obsq0Dc7mc",
                "https://www.youtube.com/watch?v=_JLwfq2WBO0",
                "https://www.youtube.com/watch?v=2E7jjf6NLy0",
                "https://www.youtube.com/watch?v=k4j_Uw5Ot6o",
            ],
        }
    ).reset_index(drop=True)
    assert search(user_input, videos).reset_index(drop=True).equals(expected)
