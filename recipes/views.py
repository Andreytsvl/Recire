from django.http import HttpResponse

from recipes.models import Recipe, Category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from recipes.forms import CreateRecipeForm
import random


def index(request):
    recipes = Recipe.objects.all()[:5]  # Получаем первые 5 рецептов
    return render(request, 'index.html', {'recipes': recipes})

def about(request):
    return render(request, 'about.html')


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Автоматически заполняем поле author
            recipe.save()
            form.save_m2m()  # Сохраняем связи с категориями
            return redirect('user:profile')  # Перенаправляем на страницу профиля
    else:
        form = CreateRecipeForm()
    categories = Category.objects.all()  # Передаём категории в шаблон
    return render(request, 'create_recipe.html', {'form': form, 'categories': categories})


def random_recipe(request):
    # Отбираем 5 случайных рецептов
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'random_recipe.html', {'recipes': recipes})
