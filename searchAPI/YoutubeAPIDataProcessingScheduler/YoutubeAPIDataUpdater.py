from apscheduler.schedulers.background import BackgroundScheduler
from searchAPI.YoutubeAPIDataProcessor import YouTubeAPIDataProcessor
from searchAPI.APIKeyManager import APIKeyManager
import logging

logger = logging.getLogger(__name__)

def start():
    """
    Start the background scheduler and save YouTube videos data.

    This method creates a BackgroundScheduler object, creates a YouTubeAPIDataProcessor object, and adds a job to the
    scheduler that runs the `save_youtube_videos_data()` method of the YouTubeAPIDataProcessor object at an interval of
    10 seconds. The job is given the ID "youtube_api_data_processor_001" and replaces any existing job with the same ID.
    Finally, the scheduler is started.
    """

    api_key_manager = APIKeyManager()
    api_key = api_key_manager.get_available_api_key()

    if api_key is None:
        logger.error("No API Key Available No Job Will Be Scheduled")
        return
    
    logger.info("Chosen API Key Is {}".format(api_key))

    scheduler = BackgroundScheduler()
    youtube_api_data_processor = YouTubeAPIDataProcessor()
    scheduler.add_job(
        lambda : youtube_api_data_processor.save_youtube_videos_data(api_key),
        "interval",
        seconds=10,
        id="youtube_api_data_processor_001",
        replace_existing=True
    )
    scheduler.start()
    logger.info("New Job Id Created Successfully At an Interval of 10 seconds")
    