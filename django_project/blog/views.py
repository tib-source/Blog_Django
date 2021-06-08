from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    context = {'posts': Article.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)
