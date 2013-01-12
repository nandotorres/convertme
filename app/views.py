# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson

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
    
    if request.method == 'POST':        
        form = VideoForm(request.POST, request.FILES)
        video = Video(file = request.FILES['file'])
        video.save()
        
        feedback["status"] = "ok"
        feedback["job_id"] = "222"
        
        return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")
    else:
        form = VideoForm()

    feedback["sttaus"] = "nok"
    feedback["job_id"] = "0"
    
    return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")