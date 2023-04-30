"""A module that performs unit tests for the youtube.py file."""
import os
import csv
import pytest
from googleapiclient.errors import HttpError  # type: ignore
from youtube import retrieve_shows

# Set up the test data
GENRES = ["Comedy", "Drama", "Action", "Horror", "Music", "Art"]
NUM_SHOWS = 5


def test_retrieve_shows():
    """Test the retrieve_shows function."""
    try:
        # Call the function to retrieve shows
        retrieve_shows(GENRES, NUM_SHOWS)

        # Check if the output file exists
        assert os.path.isfile("video_info.csv"), "Output file not found"

        # Check if the output file is not empty
        with open("video_info.csv", encoding="utf-8-sig") as csvfile:
            csv_reader = csv.reader(csvfile)
            header_row = next(csv_reader)
            assert header_row == [
                "Title",
                "Genre",
                "URL",
            ], "The output file does not contain the correct header row"
            rows = list(csv_reader)
            assert rows, "The output file is empty"

        # Check if the function returns None
        assert (
            retrieve_shows(GENRES, NUM_SHOWS) is None
        ), "The retrieve_shows function should return None"

    except HttpError as error:
        pytest.fail(f"An HTTP error occurred: {error}")
