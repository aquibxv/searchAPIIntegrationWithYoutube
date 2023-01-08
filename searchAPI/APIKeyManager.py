from searchAPIIntegrationWithYoutube.settings import API_KEYS
import requests
import datetime

class APIKeyManager:
    """
    Manager for YouTube API keys.

    This class manages a list of API keys and provides methods for checking the availability of an API key and retrieving
    an available API key.
    """
    api_key_dict = {}

    def __init__(self) :
        """
        Initialize the API key manager.

        This method initializes the `api_key_dict` attribute with the availability status of each API key.
        """
        for api_key in API_KEYS:
            self.api_key_dict[api_key] = self._is_exhausted_api_key(api_key)

    def get_available_api_key(self):
        """
        Retrieve an available API key.

        This method iterates over the list of API keys and returns the first available key. If no keys are available, it
        returns `None`.
        """

        for api_key in API_KEYS:
            if not self.api_key_dict[api_key]:
                return api_key

        return None

    def _is_exhausted_api_key(self, api_key):
        """
        Check the availability of an API key.

        This method sends a GET request to the YouTube API using the provided `api_key` and returns `True` if the key is
        available, or `False` if the key has been exhausted or is invalid.
        """

        url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&publishedAfter={}&q=cricket&type=video&key={}"
        date_now = datetime.datetime.now(tz = datetime.timezone.utc)
        publish_time = date_now.strftime('%Y-%m-%dT%H:%M:%SZ')
        response = requests.get(url.format(publish_time, api_key))

        if response.status_code == 403:
            return True
        
        return False


    