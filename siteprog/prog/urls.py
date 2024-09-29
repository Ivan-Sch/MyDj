from django.urls import path, register_converter
from . import views
from . import converters #импортируем для пользования шаблонами из файла converters.py

register_converter(converters.FourDigitYearConverter, "year4") #создаем конвертор для обращения по заголовку "year4"

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.categories, name='cats'),
    path('proger/<year4:year>/', views.proger_date, name='progdata'), #добавляем маршрут через конвертор для функции представления
    path('about/', views.about, name='about')
]