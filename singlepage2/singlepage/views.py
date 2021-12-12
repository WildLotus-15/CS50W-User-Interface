from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request, "singlepage/index.html")

texts = ['aleko midis mamukastan',
        'mamuka midis mananastan',
        'manana elodeba stumrebs']

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")