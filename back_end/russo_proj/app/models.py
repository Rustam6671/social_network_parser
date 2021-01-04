from django.db import models

# Create your models here.
class Photo(models.Model):
    photo_url = models.URLField()
    photo_likes = models.IntegerField()
    date_of_publication = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    profile_photo = models.URLField()
