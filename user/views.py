from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
#from django.db.models import Prefetch

from user.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(redirect_page)

                return HttpResponseRedirect(reverse('recipes:index'))
            else:
                messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'user/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()



            user = form.instance
            auth.login(request, user)



            messages.success(request, f"{user.username}, Вы зарегистрированы")
            return HttpResponseRedirect(reverse('recipes:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form':form
    }
    return render(request, 'user/registration.html', context)

@login_required  #запрет для незарег. пользователей
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)



    context = {
        'title': 'Home - Кабинет',
        'form': form,

    }
    return render(request, 'user/profile.html', context)



@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('recipes:index'))
