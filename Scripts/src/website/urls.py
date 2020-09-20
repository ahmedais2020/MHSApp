from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('home/',views.home, name="home"),
    path('index/',views.index, name="index"),  
    path('test/',views.test, name="test"),  
    path('GeneraLinstructions/',views.GeneraLinstructions, name="GeneraLinstructions"),
    path('OurTeam/',views.OurTeam, name="OurTeam"),



]
