# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson

from zencoder import Zencoder

from app.models import Video
from app.forms import VideoForm

"""
 upload:
   realiza upload dos arquivos para o servidor
   apos realizar o upload e salvar o registro, faz uma chamada a API do zencoder
   e retorna um json com o status e id do job 
"""
def upload(request):
    
    feedback = {} #sera usado para o retorno da acao
    
    if request.is_ajax() or request.method == 'POST':        
        form = VideoForm(request.POST, request.FILES)
        video = Video(file = request.FILES['file'])
        video.save()
        job = schedule_zencoder_job(video.file)
        
        if job.code == 201:
            feedback["status"] = "ok" 
            feedback["job_id"] = job.body['id']
            video.job_id = job.body['id']
            video.save()
        else:
            feedback["sttaus"] = "nok"
            feedback["job_id"] = "0"
        
        return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")
    else:
        form = VideoForm()

    feedback["sttaus"] = "nok"
    feedback["job_id"] = "0"
    
    return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")
    
"""
  Funcao auxiliar para criar o job no Zencoder
  Mover depois para dentro de um local mais apropriado
"""    
def schedule_zencoder_job(name = ""):
    zen = Zencoder("7f188a0403a4caac59d8a0080015cae9", api_version = "v2", as_xml = False, test = True)

    output = {}
    output["url"] = "s3://nandotorres/%s" % "teste.wmv"
    output["base_url"] = "s3://nandotorres/"
    output["filename"] = "teste.wmv"
    output["format"]   = "wmv"
    output["notifications"] = [{"url": "http://teste.com/notify"}]
    
    job = zen.job.create("http://s3.amazonaws.com/zencodertesting/test.mov", output)
    
    return job
    
"""
 Acao para que o zencoder possa notificar que um job foi concluido
"""
def notify(request, id = 0):
    video = Video.objects.get(job_id = id)
    video.job_done = True
    video.save()
    return HttpResponse(simplejson.dumps({'status': get_absolute_url()}), mimetype="application/json")