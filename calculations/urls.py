from django.urls import path
from . import views

urlpatterns = [
    path('calculate', views.calculate, name='calculate'),
    path('calc', views.calc, name='calc'),
    path('nextvalue', views.nextvalue, name='nextvalue'),
    path('series', views.series, name='series'),
    path('solve', views.solve, name='solve'),
    path('solution', views.solution, name='solution'),
    path('', views.home, name='home')
] 