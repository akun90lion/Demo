from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("This is app1")
def index1(request):
    return HttpResponse("ahihihihihihihihihihih")
