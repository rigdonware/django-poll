from django.shortcuts import render
from django.http import HttpResponse

#put views here
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")