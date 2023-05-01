"""A module that exports youtube videos into a csv file."""
import csv
import os
import googleapiclient.discovery  # type: ignore
import click  # type: ignore


@click.command()
@click.argument("output_file")
@click.option("--genres", "-g", multiple=True, required=True, help="Genres")
@click.option("--num_show", "-n", default=200, help="Number of videos")
def retrieve_shows(genres: list[str], num_show: int) -> None
    """Retrieve Youtube show information (i.e., show title, genre, and url)."""
    # Set the API credentials and parameters
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=os.environ["YOUTUBE_API"]
    )

    search_params = {
        "type": "video",
        "part": "snippet",
        "maxResults": num_show,
        "order": "relevance",
    }

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
                video_response = (
                    youtube.videos()
                    .list(part="snippet", id=video_id, hl="en_US")
                    .execute()
                )

                for video_result in video_response.get("items", []):
                    # Get the video title
                    video_title = video_result["snippet"]["title"]

                    # Get the video URL
                    video_url = f"https://www.youtube.com/watch?v={video_id}"

                    # Write the video title, genre, and URL to the CSV file
                    writer.writerow([video_title, genre, video_url])


if __name__ == "__main__":
    retrieve_shows()
