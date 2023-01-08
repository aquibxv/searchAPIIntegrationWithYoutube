from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class SearchapiConfig(AppConfig):
    """
    Configuration for the `searchAPI` Django app.

    This class extends the `AppConfig` class and overrides the `ready()` method. When the app is ready, it starts the
    `YoutubeAPIDataUpdater` class's `start()` method.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'searchAPI'

    def ready(self):
        """
        Start the `YoutubeAPIDataUpdater` class's `start()` method when the app is ready.
        """
        from .YoutubeAPIDataProcessingScheduler import YoutubeAPIDataUpdater
        logger.info("Staring YoutubeAPIDataProcessing Scheduler")
        YoutubeAPIDataUpdater.start()