# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from zencoder import Zencoder
import boto

class Video(models.Model):
    file = models.FileField(upload_to= settings.AWS_MEDIA_INPUT)
    formato = models.CharField(max_length = 5, default = 'webm')
    job_id = models.IntegerField(default=0, null=True, blank=True)
    job_done = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
         super(Video, self).save(*args, **kwargs)
         if self.file:
             conn = boto.s3.connection.S3Connection(
                                 settings.AWS_ACCESS_KEY_ID,
                                 settings.AWS_SECRET_ACCESS_KEY)
             bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
             k = boto.s3.key.Key(bucket)
             k.key = "/%s%s" % (settings.AWS_MEDIA_DIR, self.file.name)
             k.set_acl('public-read')
    
    """
      Metodo para criar um job de conversao no zencoder
    """    
    def schedule_zencoder_job(self):
        zen = Zencoder("7f188a0403a4caac59d8a0080015cae9", api_version = "v2", as_xml = False, test = True)

        output = {}
        output["url"] = "s3://%s/%s.%s" % (settings.AWS_STORAGE_BUCKET_NAME, self.file.name.split("/")[-1], self.formato)
        output["base_url"] = "s3://%s/" % settings.AWS_STORAGE_BUCKET_NAME
        output["format"]   = self.formato
        output["public"] = 1
        output["notifications"] = [{ "url": ("%s/notify/%s" % (settings.SITE_URL, self.id)) }]
    
        job = zen.job.create("s3://%s/%s%s" % (settings.AWS_STORAGE_BUCKET_NAME, settings.AWS_MEDIA_DIR, self.file.name), output)
    
        return job
        
    def __unicode__(self):
        return "Video %s" % self.job_id