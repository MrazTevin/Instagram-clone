from django.contrib import admin
from .models import Image,tag,UserProfile
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)

admin.site.register(Image)
admin.site.register(tag)
admin.site.register(UserProfile)