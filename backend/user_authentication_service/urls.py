
from django.urls import path
from . import views


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('signout/', views.sign_out, name='sign_out'),
    path('', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),

]
