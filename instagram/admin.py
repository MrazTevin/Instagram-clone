from django.contrib import admin
from .models import Image, tag, Profile, Comment
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)


admin.site.register(Image)
admin.site.register(tag)
admin.site.register(Profile)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')


admin.site.register(Comment, CommentAdmin)
