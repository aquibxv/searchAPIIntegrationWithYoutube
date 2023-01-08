import requests
import datetime
from searchAPI.models import YoutubeVideo

class YouTubeAPIDataProcessor:

    def _get_youtube_videos_data(self, api_key, published_after):

        predifined_url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&publishedAfter={}&q=cricket&type=video&key={}'.format(published_after, api_key)
        api_response = requests.get(predifined_url)
        try:
            api_response.raise_for_status()
            return api_response.json()
        except:
            return None
    
    def save_youtube_videos_data(self):
        
        api_key = 'AIzaSyCdhQ1v4sUYdxlzONcpUkIOiH_Ct591iSA'
        date_now = datetime.datetime.now(tz = datetime.timezone.utc)
        published_after = date_now - datetime.timedelta(minutes=1)
        published_after = published_after.strftime('%Y-%m-%dT%H:%M:%SZ')

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
                except Exception as e:
                    pass


    
        
        