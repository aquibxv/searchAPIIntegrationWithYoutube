from django.db import models

class YoutubeVideo(models.Model):
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