from django.urls import path, register_converter
from . import views
from . import converters #импортируем для пользования шаблонами из файла converters.py

register_converter(converters.FourDigitYearConverter, "year4") #создаем конвертор для обращения по заголовку "year4"

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('proger/<year4:year>/', views.proger_date, name='progdata'), #добавляем маршрут через конвертор для функции представления
    path('about/', views.about, name='about'),
    path('author/<int:author_id>/', views.show_author, name='author'),
]