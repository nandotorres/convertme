# -*- coding: utf-8 -*-
from django.db import models

class Video(models.Model):
    file = models.FileField(upload_to='videos/%Y/%m/%d')
    job_id = models.IntegerField(null=True, blank=True)
    job_done = models.BooleanField(default=False)