from django.contrib import admin
from .models import Channel, Category, VideoDetail, VideoFiles, ViewCount

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(VideoDetail)
admin.site.register(VideoFiles)
admin.site.register(ViewCount)
