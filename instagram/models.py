from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    comments = models.TextField()

    def __str__(self):
        return self.image_name 
