# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from zencoder import Zencoder

class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    formato = models.CharField(max_length = 5, default = 'webm')
    job_id = models.IntegerField(default=0, null=True, blank=True)
    job_done = models.BooleanField(default=False)
    
    """
      Funcao auxiliar para criar o job no Zencoder
      Mover depois para dentro de um local mais apropriado
    """    
    def schedule_zencoder_job(self):
        zen = Zencoder("7f188a0403a4caac59d8a0080015cae9", api_version = "v2", as_xml = False, test = True)

        output = {}
        output["url"] = "s3://nandotorres/%s.%s" % (self.file.name.split("/")[-1], self.formato)
        output["base_url"] = "s3://nandotorres/"
        output["format"]   = self.formato
        output["public"] = 1
        output["notifications"] = [{ "url": ("%s/notify/%s" % (settings.SITE_URL, self.id)) }]
    
        job = zen.job.create(settings.SITE_URL + settings.MEDIA_URL + self.file.name, output)
    
        return job
        
    def __unicode__(self):
        return "Video %s" % self.job_id