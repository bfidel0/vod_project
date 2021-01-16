from django import template
from vod_video.models import Channel
from django.contrib.auth import get_user_model

user = get_user_model()
register = template.Library()


@register.filter(name='has_channel')
def has_channel(user):
    try:
        channel = Channel.objects.get(user=user)
    except Channel.DoesNotExist:
        return False
    return True
