from django.db import models
from user.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    preparation_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.IntegerField(verbose_name="Время приготовления (минуты)")
    image = models.ImageField(upload_to='rec/', verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    categories = models.ManyToManyField(Category, through='RecipeCategory', verbose_name="Категории")
    #created_at = models.DateTimeField(auto_now_add=True, default=None, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Recipes'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'



class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    #author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        unique_together = ('recipe', 'category')
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категории рецептов'
    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"