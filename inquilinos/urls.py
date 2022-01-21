
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:inquilino_id>', views.inquilino, name='inquilino'),
    path('<int:unidade_id>', views.unidade, name='unidade'),
]
