from django.contrib import admin
from .models import Channel, Category, VideoDetail, VideoFiles

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(VideoDetail)
admin.site.register(VideoFiles)
