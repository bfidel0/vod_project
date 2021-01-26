from django import forms
from .models import Channel, VideoFiles
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('name', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'enter your channel name here', 'class': 'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'}),
            'category': forms.Select(attrs={'class': 'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
        }


class EditChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('name', 'channel_banner', 'channel_pic', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'enter your channel name here', 'class': 'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'}),
            'channel_banner': forms.FileInput(attrs={'class': 'border-0 mb-2 outline-none'}),
            'channel_pic': forms.FileInput(attrs={'class': 'border-0 mb-4 outline-none'}),
            'description': forms.Textarea(attrs={'class': 'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
        }


class VideoSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})
