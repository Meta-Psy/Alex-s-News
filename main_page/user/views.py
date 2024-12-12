from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginFrom, UserRegisterForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'registration.html',
                          {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'registration.html',
                      {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на домашнюю страницу
            else:
                # Если пользователь не найден
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Неверное имя пользователя или пароль'
                })
        else:
            # Если форма не валидна
            return render(request, 'login.html', {'form': form})
    else:
        # GET запрос
        form = UserLoginFrom()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('about')
