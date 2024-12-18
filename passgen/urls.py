"""
URL configuration for passgen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import chat_box
urlpatterns = [
    path('index/', views.index, name="main page"),
    path('generate/', views.password_generator_view, name='password generator'),
    path('generate/<str:password_id>/', views.password_detail_view, name='password_detail'),
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
]
