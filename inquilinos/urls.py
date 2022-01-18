
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inquilino', views.inquilino, name='inquilino'),
    path('unidade', views.unidade, name='unidade'),
]
