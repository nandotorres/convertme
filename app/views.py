# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.models import Video
from app.forms import VideoForm
    
def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Document(file = request.FILES['file'])
            video.save()

            return HttpResponseRedirect(reverse('app.views.upload'))
    else:
        form = VideoForm()

    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request)
    )