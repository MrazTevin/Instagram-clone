from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import UserManager

User = get_user_model()
# Create your models here.


class tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=255)
    tags = models.ManyToManyField(tag)
    image = models.ImageField(upload_to='photos/', blank=True)
    profile = models.ForeignKey(User, blank=True, default=1)
    post = HTMLField()

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
    def get_image(cls):
        return cls.objects.get(id=1)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments')
    user = models.CharField(max_length=250)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def approved(self):
        self.approved = True
        self.save()
