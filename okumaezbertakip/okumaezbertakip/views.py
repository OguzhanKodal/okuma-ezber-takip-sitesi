from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    sablon = loader.get_template('index.html')
    return HttpResponse(sablon.render())