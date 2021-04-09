from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def todo(response):
    return HttpResponse("<center><h1>TO DO LIST</h1></center>")
