from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Youtube Data Analysis")


def youtube_auth(request):
    return HttpResponse("Facebook Data Analysis")