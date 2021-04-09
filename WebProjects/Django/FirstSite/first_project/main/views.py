from django.shortcuts import render
from django.http import HttpResponse
from .models import People
# Create your views here.

def index(response):
    return HttpResponse("Hello World")
def name(response, name):
    try:
        p = People.objects.get(name=name)
        return HttpResponse(f"Hello {p.name} {p.surname}")
    except Exception as e:
        return HttpResponse("There is no user with this name in our database!")
