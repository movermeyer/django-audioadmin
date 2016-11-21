# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from django.template import Context
from django.db.models.signals import post_save

from mutagen.easyid3 import EasyID3

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from validators import MimetypeValidator

try:
    from django.apps import apps as django_apps
except ImportError:
    django_apps = None


def get_audio_upload_path(obj, filename):
    obj.name = filename
    return os.path.join("audio", obj.user.username, filename)


def get_artwork_upload_path(obj, filename):
    return os.path.join("artwork", obj.user.username, filename)


class AudioFile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="audiofiles")
    file = models.FileField(
        upload_to=get_audio_upload_path,
        validators=[MimetypeValidator([
            'audio/mpeg', 'audio/x-m4a',
            'audio/mp3', 'audio/wav',
            'audio/aiff', 'audio/x-wav', 'audio/x-aiff'])])
    name = models.CharField(
        _("Original Filename"), max_length=200, null=True, blank=True)
    title = models.CharField(
        _("Title"), max_length=200, null=True, blank=True)
    artist = models.CharField(
        _("Artist"), max_length=200, null=True, blank=True)
    album = models.CharField(
        _("Album"), max_length=200, null=True, blank=True)
    artwork = models.ImageField(
        upload_to=get_artwork_upload_path, null=True, blank=True)
    artwork_thumb = ImageSpecField(
        source='artwork', processors=[
            ResizeToFill(150, 150)], format='JPEG', options={'quality': 90})
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.file)

    def url(self):
        return "%s%s" % (settings.MEDIA_URL, self.file)

    def display_name(self):
        if self.artist and self.title:
            return "%s-%s" % (self.artist, self.title)
        else:
            return self.name

    def audio_preview(self):
        html = get_template('player.html').render(
            Context({
                'obj': self
            })
        )
        return html

    audio_preview.allow_tags = True

    def thumbnail(self):
        if self.artwork:
            return '<img src="%s"/>' % self.artwork_thumb.url
        else:
            return '<img src="http://placehold.it/150x150"/>'

    thumbnail.allow_tags = True


def fetch_id3(sender, instance, created, **kwargs):
    """Fetch id3 tags."""
    if created:
        try:
            id3 = EasyID3("%s/%s" % (settings.MEDIA_ROOT, instance.file))
        except:
            pass
        try:
            instance.title = id3['title'][0]
        except:
            pass
        try:
            instance.artist = id3['artist'][0]
        except:
            pass
        try:
            instance.album = id3['album'][0]
        except:
            pass
        instance.save()


post_save.connect(fetch_id3, sender=AudioFile, dispatch_uid="fetch_id3")
