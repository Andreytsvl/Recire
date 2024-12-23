from django.http import HttpResponse
from django.db.models import Q
from recipes.models import Recipe, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recipes.forms import CreateRecipeForm
import random
from django.core.paginator import Paginator

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

def list_recipes(request):
    # Фильтры
    title_filter = request.GET.get('title', '')
    author_filter = request.GET.get('author', '')
    category_filter = request.GET.get('category', '')

    # Базовый запрос
    recipes = Recipe.objects.all()

    # Применение фильтров
    if title_filter:
        recipes = recipes.filter(title__icontains=title_filter)
    if author_filter:
        recipes = recipes.filter(author__username__icontains=author_filter)
    if category_filter:
        recipes = recipes.filter(categories__id=category_filter)

    # Пагинация
    paginator = Paginator(recipes, 10)  # Показывать по 10 рецептов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Получение списка категорий для фильтров
    categories = Category.objects.all()

    return render(request, 'list_recipes.html', {
        'page_obj': page_obj,
        'categories': categories,
        'title_filter': title_filter,
        'author_filter': author_filter,
        'category_filter': category_filter,
    })

@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Проверка, что текущий пользователь является автором рецепта
    if recipe.author != request.user:
        return redirect('recipes:list_recipes')

    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:list_recipes')
    else:
        form = CreateRecipeForm(instance=recipe)

    return render(request, 'update_recipe.html', {'form': form, 'recipe': recipe})

def mono_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'mono_recipe.html', {'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
    return redirect('recipes:list_recipes')