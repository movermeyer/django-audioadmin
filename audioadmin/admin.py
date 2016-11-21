# -*- coding: utf-8 -*-
from django.contrib import admin
from audioadmin.models import AudioFile


class AudioFileAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail', 'audio_preview', 'title',
        'artist', 'album', 'created', 'user')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Edit view."""
        self.fields = ('user', 'file', 'artwork', 'title', 'artist', 'album')
        return super(AudioFileAdmin, self).change_view(request, object_id)

    def add_view(self, request, form_url='', extra_context=None):
        """Add new."""
        self.fields = ('user', 'file')
        return super(AudioFileAdmin, self).add_view(request)


AudioFileAdmin.change_list_template = 'admin/change_list_extended.html'
admin.site.register(AudioFile, AudioFileAdmin)
