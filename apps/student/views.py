from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')  # Перенаправление на страницу со списком пользователей
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'delete_user.html', {'user': user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile.html', {'user': user})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            logins = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            # Замените 'login' на имя поля вашей модели пользователя, если оно отличается
            user = authenticate(request, login=logins, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_profile', user_id=user.id)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Предполагаем, что у вас есть URL с именем 'login'




def tariff_list(request):
    tariffs = Tariff.objects.all()
    return render(request, 'tariff_list.html', {'tariffs': tariffs})

def tariff_create(request):
    form = TariffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tariff_list')
    return render(request, 'tariff_form.html', {'form': form})

def tariff_update(request, pk):
    tariff = get_object_or_404(Tariff, pk=pk)
    form = TariffForm(request.POST or None, instance=tariff)
    if form.is_valid():
        form.save()
        return redirect('tariff_list')
    return render(request, 'tariff_form.html', {'form': form})

def tariff_delete(request, pk):
    tariff = get_object_or_404(Tariff, pk=pk)
    if request.method == 'POST':
        tariff.delete()
        return redirect('tariff_list')
    return render(request, 'tariff_confirm_delete.html', {'tariff': tariff})

def tariff_view(request, pk):
    tariff = get_object_or_404(Tariff, pk=pk)
    return render(request, 'tariff_view.html', {'tariff': tariff})


def home(request):
    return render(request, 'home.html')