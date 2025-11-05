from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from main.models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),

        )

        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')

@never_cache
def logout_view(request):
    logout(request)
    return redirect('home')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('password1'):
            user = User.objects.filter(username=request.POST.get('username'))
            if user.exists():
                return redirect('home')
            else:
                user = User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password'),
                )
                login(request,user)
                return redirect('home')
        return redirect('register')
