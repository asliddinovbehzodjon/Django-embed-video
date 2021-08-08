from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=False)
    url=EmbedVideoField()
    def __str__(self):
        return self.title