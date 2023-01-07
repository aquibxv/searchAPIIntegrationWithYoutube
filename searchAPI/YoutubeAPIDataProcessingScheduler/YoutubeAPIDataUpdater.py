from apscheduler.schedulers.background import BackgroundScheduler
from searchAPI.YoutubeAPIDataProcessor import YouTubeAPIDataProcessor

def start():
    scheduler = BackgroundScheduler()
    youtube_api_data_processor = YouTubeAPIDataProcessor()
    scheduler.add_job(
        youtube_api_data_processor.save_youtube_videos_data,
        "interval",
        seconds=10,
        id="youtube_api_data_processor_001",
        replace_existing=True
    )
    scheduler.start()