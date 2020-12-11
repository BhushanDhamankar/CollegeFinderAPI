from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    
    path('', views.showcategory, name="showcategory"),
    path('home', views.showcategory, name="showcategory"),
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('feedback', views.feedback, name="feedback"),
    path('FindCollege', views.FindCollege, name="FindCollege"),

    

]
