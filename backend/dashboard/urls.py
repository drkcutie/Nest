from django.urls import path
from .views import DashboardView, UserSettingsView, UploadImageView,DashboardNestView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('<int:id>/', DashboardNestView.as_view(), name='dashboard-nest-tab'),  
    path('settings/', UserSettingsView.as_view(), name='user_settings'),
    path('settings/upload/', UploadImageView.as_view(), name='upload_image'),
]



