"""A module that performs unit tests for the youtube.py file."""
import os
import csv
import pytest  # type: ignore
from googleapiclient.errors import HttpError  # type: ignore
from click.testing import CliRunner
from youtube import retrieve_shows  # type: ignore


# Set up the test data
GENRE1 = "Comedy"
GENRE2 = "Drama"
NUM_SHOWS = 50
OUTPUT_PATH = "videos.csv"


def test_retrieve_shows():
    """Test the retrieve_shows function."""
    try:
        # Call the function to retrieve shows
        runner = CliRunner()
        result = runner.invoke(
            retrieve_shows,
            [
                "--genres",
                GENRE1,
                "--genres",
                GENRE2,
                "--num_show",
                str(NUM_SHOWS),
                OUTPUT_PATH,
            ],
        )
        print(result.output)

        # Check if the command ran successfully
        assert result.exit_code == 0, "The command did not run successfully"

        # Check if the output file exists
        assert os.path.isfile(OUTPUT_PATH), "Output file not found"

        # Check if the output file is not empty
        with open(OUTPUT_PATH, encoding="utf-8-sig") as csvfile:
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
            result.return_value is None
        ), "The retrieve_shows function should return None"

    except HttpError as error:
        pytest.fail(f"An HTTP error occurred: {error}")
