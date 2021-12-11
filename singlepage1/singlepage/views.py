from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

def index(request):
    return render(request, "singlepage/index.html")

texts = ["aleko midis mamukastan",
        "mamuka midis mananastan",
        "mananas mostyvnia kargis traki"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        return Http404("No such section")