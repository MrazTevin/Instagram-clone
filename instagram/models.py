from django.db import models

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=255)
    comments = models.TextField()
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return self.image_name 
