from django.urls import path

from . import views

app_name = 'datas'

urlpatterns = [
    path('', views.index, name='index'),
]
