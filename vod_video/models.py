import uuid
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Quick little function for directory of video files unique to channel


def channel_directory_path(instance, filename):
    return "video_files/channel_{0}/{1}".format(instance.channel.id, filename)


# Import Custom User
User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_banner = models.ImageField(
        upload_to='channel/', default='default_banner.jpg')
    channel_pic = models.ImageField(
        upload_to='profile/', default='default_picture.jpg')
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VideoFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='channel_directory_path')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"video_file{self.id}"

    def get_absolute_url(self):
        return reverse('video_watch', args=[str(self.id)])


class VideoDetail(models.Model):
    videofile = models.OneToOneField(VideoFiles, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    visibility = models.BooleanField(
        choices=((False, 'private'), (True, 'public')))
    thumbnail = models.ImageField(upload_to='thumbnail/')

    def __str__(self):
        return self.title


class ViewCount(models.Model):
    video = models.ForeignKey(
        VideoFiles, related_name='view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=50)
    session = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ip_address}'
