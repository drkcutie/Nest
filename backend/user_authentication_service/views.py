import os

from django.contrib import messages
# from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,authenticate, login, logout
from .forms import RegisterForm, LoginForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests


User = get_user_model()



class MyTokenObtainPairView(TokenObtainPairView):
    # You can customize the serializer if needed
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass






def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")  # Debugging print

            # Check if user exists before authenticating
            try:
                user_check = User.objects.get(username=username)
                print(f"User {username} found in the database.")
            except User.DoesNotExist:
                print(f"User {username} does not exist in the database.")
                messages.error(request, 'User does not exist.')
                return render(request, 'user_auth/login.html', {'form': form})

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_data'] = {'username': user.username, 'email': user.email}

                # refresh = RefreshToken.for_user(user)
                # return render(request, 'user_auth/welcome.html', {
                #     'access': str(refresh.access_token),
                #     'refresh': str(refresh),
                # })
                print(f"User {username} authenticated successfully.")
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                print(f"Authentication failed for user: {username}")
                messages.error(request, 'Invalid username or password.')
        else:
            print("Form data is invalid.")
    else:
        form = LoginForm()

    return render(request, 'user_auth/login.html', {'form': form})






def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_user')
        else:

            messages.error(request, "Username, email, or password is invalid.")
    else:
        form = RegisterForm()

    return render(request, 'user_auth/register.html', {'form': form})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def welcome(request):
    return render(request, 'user_auth/welcome.html')
    #  return Response({"message": "Welcome to the protected route!"})


def logout_view(request):
    if 'user_data' in request.session:
        del request.session['user_data']
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')





# GOOGLE AUTHENTICATION
@csrf_exempt
def sign_in(request):
    return render(request, 'user_auth/sign_in.html')


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    print(token)
    print(os.environ['GOOGLE_OAUTH_CLIENT_ID'])
  
    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
        print("user: " , user_data)
    except ValueError as e:
        
        print(e)
        return HttpResponse(status=403)
    
    

    # In a real app, I'd also save any new user here to the database.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('sign_in')


def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')
