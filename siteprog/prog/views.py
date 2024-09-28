from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):  # Class HttpRequest
    return HttpResponse("Вы на главной странице")


def categories(request):
    return HttpResponse("<h1>Темы по категориям</h1>")


def proger_date(request, year):
    """Для конвертора класса FourDigitYearConverter"""
    return HttpResponse(f"<h1>Программисты</h1> <p>года: {year}")
