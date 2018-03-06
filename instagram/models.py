from django.db import models

# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=255)
    comments = models.TextField()
    tags = models.ManyToManyField(tag)




    def __str__(self):
        return self.image_name 
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls):
        return cls.objects.update()
   
    @classmethod
    def image(cls):
       return cls.objects.get(id=1)
   