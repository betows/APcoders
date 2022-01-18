
from django.contrib import admin
from django.urls import path, include

import inquilinos

urlpatterns = [
    path('', include('inquilinos.urls')),
    path('admin/', admin.site.urls),
]
