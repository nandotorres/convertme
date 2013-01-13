# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import simplejson

from zencoder import Zencoder

from app.models import Video
from app.forms import VideoForm
from django.test import TestCase


class SimpleTest(TestCase):
    """
     Testando o response da index
    """ 
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    """
     Testando criar um video
    """
    def test_criar_video(self):
        self.video = Video(formato = 'WEBM', file = "%stestes/video_teste.mp4" % settings.MEDIA_URL)
        self.video.save()
        self.assertNotEqual(self.video.id, 0)
        self.assertEqual(self.video.formato, 'WEBM')
        self.assertEqual(self.video.file.name, "%stestes/video_teste.mp4" % settings.MEDIA_URL)
    
    """
     Testando o retorno de um job enviado para o zencoder
    """
    def test_job_zencoder(self):
        self.video = Video(formato = 'webm', file = "%stestes/video_teste.mp4" % settings.MEDIA_URL)
        self.video.save()
        self.job = self.video.schedule_zencoder_job()
        self.assertNotEqual(self.job.body['id'], 0)
        self.assertEqual(self.job.code, 201)
        self.assertEqual(self.job.body['outputs'][0]['url'], "http://nandotorres.s3.amazonaws.com/video_teste.mp4.webm")        

