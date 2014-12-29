# -*- coding: utf-8 -*-
import os
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from audioadmin.models import AudioFile

class AudioFileModel(TestCase):

    def setUp(self):
        User.objects.create(username="admin")
        

    def test_valid__mimetype_upload(self):
        user = User.objects.get(username='admin')
        upload_file = open(os.path.dirname(__file__) + '/data/test.mp3', 'rb')
        audiofile = AudioFile(
            name='Test Audio',
            file=SimpleUploadedFile(upload_file.name, upload_file.read()),
            user=user
        )
        
        audiofile.save()
        audiofile.full_clean()



    def test_invalid_mimetype_upload(self):
        user = User.objects.get(username='admin')
        upload_file = open(os.path.dirname(__file__) + '/data/test.txt', 'rb')
        audiofile = AudioFile(
            name='Test Audio',
            file=SimpleUploadedFile(upload_file.name, upload_file.read()),
            user=user
        )

        with self.assertRaises(ValidationError): 
            audiofile.save()
            audiofile.full_clean()

   