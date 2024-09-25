from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .forms import RegisterForm, LoginForm

User = get_user_model()


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Testing form")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username).first()
            if user is None:
                messages.error(request, 'Username does not exist.')
                return HttpResponseRedirect("Invalid credentials", status=401)
            if not user.check_password(password):
                messages.error(request, 'Incorrect password.')
                return HttpResponseRedirect("Invalid credentials", status=401)

            messages.success(request, 'Login successful!')
            print("Success")
            return redirect('welcome')

    return render(request, 'user_auth/login.html')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            print("test")
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match.')

                return HttpResponseRedirect("Password does not exist", status=401)
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username "%s" is already in use.' % username)
                return HttpResponseRedirect("Password does not exist", status=401)
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email "%s" is already in use.' % email)
                return HttpResponseRedirect("Password does not exist", status=401)
            else:
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=make_password(password)
                )
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                print("Success")
                return redirect('login_user')
    else:
        form = RegisterForm()
        print("Failed")

    return render(request, 'user_auth/register.html', {'form': form})


def welcome(request):
    return render(request, 'user_auth/welcome.html')
