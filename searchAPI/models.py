from django.db import models

class YoutubeVideo(models.Model):
    """
    A model representing a YouTube video.

    This class extends the `models.Model` class and represents a YouTube video with the following fields:
        - `video_id`: The ID of the video.
        - `channel_id`: The ID of the channel that uploaded the video.
        - `title`: The title of the video.
        - `description`: The description of the video.
        - `published_at`: The date and time that the video was published.
        - `publish_time`: The date and time that the video was saved to the database.
        - `channel_title`: The title of the channel that uploaded the video.
        - `thumbnail_url`: The URL of a thumbnail image for the video.

    The `YoutubeVideo` model has indexes on the `-publish_time`, `title`, and `description` fields to improve performance
    when retrieving and searching for videos.
    """
    video_id = models.CharField(max_length=100, primary_key=True) 
    channel_id = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()
    published_at = models.DateTimeField()
    publish_time = models.DateTimeField()
    channel_tile = models.CharField(max_length=100)
    thumbnail_url = models.URLField() #As there are multiple thumbnails comming in the response of 
                                     #Api therefore it makes more sense to create a new table for this 
                                     #and add foreign key but for simplicity I are taking only one.
    
    def __str__(self):
        return self.title
        
    class Meta:
        #using -publishTime as per the requirement wich will make reterival in descending order faster.
        #Adding indexes for title and description for making searching faster using title and description.
        indexes = [
            models.Index(fields=['-publish_time']),
            models.Index(fields=['title']),
            models.Index(fields=['description'])
        ]