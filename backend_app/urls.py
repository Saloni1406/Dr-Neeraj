"""
URL configuration for HCI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from backend_app import views

urlpatterns = [
    path("", views.index, name = 'Home'),
    path("AboutUs/",views.about,name = "about"),
    path("BrainTumour/",views.brain,name = "brain"),
    path("BreastCancer/",views.breast,name = "breast"),
    path("EndometriumCancer/",views.endometrium,name = "endometrium"),
    path("EsophagusCancer/",views.esophagus,name = "esophagus"),
    path("Head&Neck/",views.head,name = "head"),
    path("LungCancer/",views.lung,name = "lung"),
    path("PancreasCancer/",views.pancreas,name = "pancreas"),
    path("ProstateCancer/",views.prostate,name = "prostate"),
    path("RectumCancer/",views.rectum,name = "rectum"),
    path("StomachCancer/",views.stomach,name = "stomach"),
    path("Uterus&Cervix/",views.uterus,name = "uterus"),
    path('Home/' , views.home , name = "home"),
    
]
