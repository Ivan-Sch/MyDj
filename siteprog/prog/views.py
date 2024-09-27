from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):  # Class HttpRequest
    return HttpResponse("Вы на главной странице")


def categories(request):
    return HttpResponse("<h1>Темы по категориям</h1>")
