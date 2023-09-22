from django.urls import path
from . import views
from django.urls import  re_path
from .views import *
from rest_framework import routers
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Other URL patterns
    path('register/a', views.register_etudiant, name='register_etudiant'),
    path('getallEtud/a', views.get_all_etudiants, name='get_all_etudiants'),
     path('getallCourses/a', views.get_all_cours, name='get_all_cours'),
]