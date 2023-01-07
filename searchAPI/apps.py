from django.apps import AppConfig


class SearchapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'searchAPI'

    def ready(self):
        print("Starting Scheduler")
        from .YoutubeAPIDataProcessingScheduler import YoutubeAPIDataUpdater
        YoutubeAPIDataUpdater.start()