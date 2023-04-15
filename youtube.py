"""A module that exports youtube videos into a csv file."""
import csv
import os
import googleapiclient.discovery
from langdetect import detect


def retrieve_shows(genres: list[str], num_show: int) -> None:
    """Retrieve Youtube show information (i.e., show title, genre, and url)."""
    # Set the API credentials and parameters
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=os.environ['YOUTUBE_API'])
    search_params = {
        "type": "video",
        "part": "snippet",
        "maxResults": num_show,
        "order": "relevance"
    }

    # Set the output CSV file name
    output_file = "video_info.csv"

    # Open the output file for writing
    with open(output_file, "w", newline="", encoding="utf-8-sig") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the header row to the CSV file
        writer.writerow(["Title", "Genre", "URL"])

        # Loop over each genre
        for genre in genres:
            # Set the genre search parameter
            search_params["q"] = genre
            # Search for videos and add the results to the CSV file
            search_response = youtube.search().list(**search_params).execute()
            for search_result in search_response.get("items", []):
                # Get the video ID and retrieve the video information
                video_id = search_result["id"]["videoId"]
                video_response = youtube.videos().list(
                    part="snippet",
                    id=video_id,
                    hl="en_US"
                ).execute()
                for video_result in video_response.get("items", []):
                    # Get the video title
                    video_title = video_result["snippet"]["title"]
                    # Detect the language of the title
                    lang = detect(video_title)
                    # Check if the title is in English
                    if lang == "en":
                        # Remove non-English characters from the title
                        video_title = ''.join(
                            char for char in video_title if ord(char) < 128)
                        # Get the video URL
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        # Write the video title, genre, and URL to the CSV file
                        writer.writerow([video_title, genre, video_url])


if __name__ == "__main__":
    retrieve_shows(["Comedy", "Drama", "Action", "Horror"], 200)
