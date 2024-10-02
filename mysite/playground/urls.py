
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page),
    path('hello/', views.say_hello_To),
    path('submit/', views.home_page),
    path('login/', views.login_user),
]