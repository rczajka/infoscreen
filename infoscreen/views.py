from datetime import datetime, timedelta
import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import InfoBoxForm
from .models import InfoBox

def home(request):
    root = os.path.join(settings.MEDIA_ROOT, "infoscreen/slides")
    slides = [os.path.join(settings.MEDIA_URL, "infoscreen/slides", slide) for slide in os.listdir(root)]
    return render(request, "infoscreen/home.html", {"slides": slides})

@permission_required("infoscreen.change_infobox")
def set_info(request, slug):
    info = InfoBox.get(slug)
    if request.method == "POST":
        form = InfoBoxForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = InfoBoxForm(instance=info)
    return render(request, "infoscreen/set.html", {
        "form": form,
        "info": info
    })

def state(request, slug):
    info = InfoBox.get(slug)
    body = info.body.strip()
    if body:
        if datetime.now() > info.stamp + timedelta(seconds=info.seconds):
            body = ''
    return HttpResponse(body.replace("\n", "<br/>"), mimetype="text/plain")
