from django.urls import path, register_converter
from . import views
from . import converters #импортируем для пользования шаблонами из файла converters.py

register_converter(converters.FourDigitYearConverter, "year4") #создаем конвертор для обращения по заголовку "year4"

urlpatterns = [
    path('', views.index),
    path('cats/', views.categories),
    path('proger/<year4:year>/', views.proger_date), #добавляем маршрут через конвертор для функции представления
]