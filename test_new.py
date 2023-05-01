import os
import csv
import pytest
from googleapiclient.errors import HttpError
from youtube import retrieve_shows
import click
from click.testing import CliRunner


GENRES = ["Comedy", "Drama", "Action", "Horror", "Music", "Art"]
NUM_SHOWS = 5


def test_retrieve_shows(cli_runner):
    """Test the retrieve_shows function."""
    try:
        # Call the function to retrieve shows
        result = cli_runner.invoke(
            retrieve_shows, ["--genres", *GENRES, "--num_show", str(NUM_SHOWS), "video_info.csv"]
        )

        # Check if the command ran successfully
        assert result.exit_code == 0, "The command did not run successfully"

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

    except HttpError as error:
        pytest.fail(f"An HTTP error occurred: {error}")
