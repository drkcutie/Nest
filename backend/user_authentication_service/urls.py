
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register'),

    path('welcome/', views.welcome, name='welcome'),

]
