# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
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
    
    if request.is_ajax() or request.method == 'POST':        
        form = VideoForm(request.POST, request.FILES)
        video = Video(file = request.FILES['file'])
        video.formato = request.POST['formato']
        video.save()
        job = video.schedule_zencoder_job()
        
        if job.code == 201:
            feedback["status"] = "201" 
            feedback["job_id"] = job.body['id']
            feedback["video_id"] = video.id
            video.job_id = job.body['id']
            video.save()
        else:
            feedback["status"] = "422"
            feedback["job_id"] = "0"
        
        return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")
    else:
        form = VideoForm()

    feedback["status"] = "nok"
    feedback["job_id"] = "0"
    
    return HttpResponse(simplejson.dumps(feedback), mimetype="application/json")
    
"""
 Acao para que o zencoder possa notificar que um job foi concluido
"""
@csrf_exempt
def notify(request, video_id = 0):
    video = Video.objects.get(id = video_id)
    video.job_done = True
    video.save()
    return HttpResponse(simplejson.dumps({'status': 'ok'}), mimetype="application/json")

"""
 Acao para que o applicativo possa verificar se um video esta' com status job_done = 1
"""
def verify(request, video_id = 0):
    video = Video.objects.get(id = video_id)
    return HttpResponse(simplejson.dumps({'job_done': video.job_done}), mimetype="application/json")
        
"""
 Carrega a interface do player para assistir a um video
"""

def player(request, video_id = 0):
    video = Video.objects.get(id = video_id) 
    return TemplateResponse(request, 'player.html', {'video': video, 'nome_arquivo': gerar_nome_arquivo(video) })
    
"""
 Funcao auxliar para gerar o nome do arquivo a ser reproduzido
 recebe o nome do arquivo enviado e adiciona a extensao desejada
"""

def gerar_nome_arquivo(video_obj):
    return "%s.%s" % (video_obj.file.name.split("/")[-1], video_obj.formato)