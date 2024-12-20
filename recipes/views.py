from django.http import HttpResponse

from recipes.models import Recipe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from recipes.forms import CreateRecipeForm
import random


def index(request):
    recipes = Recipe.objects.all()[:5]  # Получаем первые 5 рецептов
    return render(request, 'index.html', {'rec': recipes})

def about(request):
    return render(request, 'about.html')


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Связываем рецепт с текущим пользователем
            recipe.save()
            return redirect('profile')  # Перенаправляем на страницу профиля
    else:
        form = CreateRecipeForm()

    return render(request, 'create_recipe.html', {'form': form})

def random_recipe(request):
    # Отбираем 5 случайных рецептов
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'random_recipe.html', {'rec': recipes})
