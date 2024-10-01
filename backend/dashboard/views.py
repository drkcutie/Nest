from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')  


def user_settings(request):
    return render(request, 'dashboard/user_settings.html')