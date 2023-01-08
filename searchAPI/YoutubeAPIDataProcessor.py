import requests
import datetime
from searchAPI.models import YoutubeVideo
from searchAPI.APIKeyManager import APIKeyManager
import logging

logger = logging.getLogger(__name__)

class YouTubeAPIDataProcessor:
    """
    Processor for YouTube API data.

    This class contains methods for fetching and saving YouTube data from the YouTube API.
    """
    def _get_youtube_videos_data(self, api_key, published_after):
        """
        Fetch YouTube videos data from the API.

        This method sends a GET request to the YouTube API using the provided `api_key` and `published_after` parameters,
        and returns the JSON response. If the request fails, it returns `None`.

        Args:
            api_key (str): The API key to use for the request.
            published_after (str): A string in the format '%Y-%m-%dT%H:%M:%SZ' representing the minimum published date
                and time to include in the response.

        Returns:
            dict: The JSON response from the API, or `None` if the request failed.
        """
        if api_key is None:
            logger.error("Exhausted the qouta for all the availabe API Keys no data will be fetched")
            raise Exception("No API Keys Availabe Haing Qouta To Fetch Data")

        predifined_url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&publishedAfter={}&q=cricket&type=video&key={}'.format(published_after, api_key)
        logger.info("Requesting data from url : {}".format(predifined_url))
        api_response = requests.get(predifined_url)
        try:
            api_response.raise_for_status()
            logger.info("Resopnse received successfully \n {}".format(api_response.json))
            return api_response.json()
        except:
            logger.error("Error while fetching data from youtube api \n {}".format(api_response.json))
            if api_response.status_code == 403:
                api_key_manager = APIKeyManager()
                api_key = api_key_manager.get_available_api_key()
            return None
    

    def save_youtube_videos_data(self, api_key):
        """
        Fetch and save YouTube videos data from the API.

        This method fetches YouTube videos data from the API using the `_get_youtube_videos_data()` method and saves the
        data to the `YoutubeVideo` model.
        """
        date_now = datetime.datetime.now(tz = datetime.timezone.utc)
        published_after = date_now - datetime.timedelta(minutes=1)
        published_after = published_after.strftime('%Y-%m-%dT%H:%M:%SZ')

        logger.info("Calling _get_youtube_videos_data for getting Youtube Videos Data")

        youtube_video_data = self._get_youtube_videos_data(api_key, published_after)

        if youtube_video_data is not None:
            for item in youtube_video_data['items']:
                try:
                    youtube_video_object = YoutubeVideo.objects.create(
                        video_id = item['id']['videoId'],
                        channel_id = item['snippet']['channelId'],
                        title = item['snippet']['title'],
                        description = item['snippet']['description'],
                        published_at = item['snippet']['publishedAt'],
                        publish_time = item['snippet']['publishTime'],
                        channel_tile = item['snippet']['channelTitle'],
                        thumbnail_url = item['snippet']['thumbnails']['default']['url']
                    )
                    youtube_video_object.save()
                    logger.info("Saved an item {} to database ".format(youtube_video_object.values()))
                except Exception as e:
                    logger.error("Exception Caught while Saving item to database {}".format(e))
                    pass


    
        
        