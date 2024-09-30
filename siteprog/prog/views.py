from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'auth': 'Сергей Балакириев', 'content': 'Учебные материалы по программиравнию', 'them_is_Python': True},
    {'id': 2, 'auth': 'Борис Годунов', 'content': 'Учебные материалы по SQL', 'them_is_Python': False},
    {'id': 3, 'auth': 'Васильев А.Н.', 'content': 'Учебные материалы по НС', 'them_is_Python': True},
]


def index(request):  # Class HttpRequest
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'author': data_db,

    }
    # return HttpResponse("Вы на главной странице")
    return render(request, 'prog/index.html', context=data)


def categories(request):
    """prog.views.path(/cats)"""
    return HttpResponse("<h1>Темы по категориям</h1>")


def addpage(request):
    """Для добавления новой страницы"""
    return HttpResponse("<h1>Добавление страницы</h1>")


def contact(request):
    """Контакты"""
    return HttpResponse("Контакты")


def login(request):
    """Авторизация"""
    return HttpResponse("Авторизация")


def proger_date(request, year):
    """Для конвертора класса FourDigitYearConverter"""
    if year > 2024:
        uri = reverse(proger_date, args=[2023])  # для назначения url маршрута (нельзя прописывать готовый URL маршрут)
        return HttpResponsePermanentRedirect(uri)  # возвращает постоянный адрес (перенаправляет на постоянный)
        # return redirect(index) #перенаправляет- через данную ГИБКУЮ ф-ю, можно вызвать ф-ю представления, написать сразу маршрут, или через имя маршрута

    return HttpResponse(f"<h1>Программисты</h1> <p>года: {year}</p>")


def page_not_found(request, exception):
    """Для ошибки 404"""
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def about(request):
    """О сайте"""
    data = {
        'title': 'Главная страница',
        'menu': ['main', 'addpage', 'contact', 'about'],
        'show_menu': True,
    }
    return render(request, 'prog/about.html/', context=data)

def show_author(request, author_id):
    """Страница автора"""
    return HttpResponse(f"Отображение автора с id={author_id}")
