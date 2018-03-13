from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()
# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=255)
    comments = models.TextField()
    tags = models.ManyToManyField(tag)
    image = models.ImageField(upload_to='photos/', blank=True)
    userprofile = models.ForeignKey(User,blank = True, default=1)
    post = HTMLField(blank = True)

    def __str__(self):
        return self.image_name2

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls):
        return cls.objects.update()
   
    @classmethod
    def get_image(cls):
       return cls.objects.get(id=1)
   
class UserProfile(models.Model):
   profile_photo = models.ImageField(upload_to='photos/', blank = True)
   first_name = models.CharField(max_length =30)
   last_name = models.CharField(max_length = 30)
   email  = models.EmailField()
   
   def __str__(self):
       return self.first_name
    
   def save_userprofile(self):
        self.save()

