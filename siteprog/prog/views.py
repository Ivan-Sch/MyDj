from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse


# Create your views here.


def index(request):  # Class HttpRequest
    # return HttpResponse("Вы на главной странице")
    return render(request, 'prog/index.html')

def categories(request):
    """prog.views.path(/cats)"""
    return HttpResponse("<h1>Темы по категориям</h1>")


def proger_date(request, year):
    """Для конвертора класса FourDigitYearConverter"""
    if year > 2024:
        uri = reverse(proger_date, args=[2023]) #для назначения url маршрута (нельзя прописывать готовый URL маршрут)
        return HttpResponsePermanentRedirect(uri) #возвращает постоянный адрес (перенаправляет на постоянный)
        # return redirect(index) #перенаправляет- через данную ГИБКУЮ ф-ю, можно вызвать ф-ю представления, написать сразу маршрут, или через имя маршрута

    return HttpResponse(f"<h1>Программисты</h1> <p>года: {year}</p>")


def page_not_found(request, exception):
    """Для ошибки 404"""
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def about(request):
    """О чем"""
    return render(request, 'prog/about.html/')
