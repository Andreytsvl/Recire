from django.db import models
from user.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    preparation_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.IntegerField(verbose_name="Время приготовления (минуты)")
    image = models.ImageField(upload_to='rec/', verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    #created_at = models.DateTimeField(auto_now_add=True, default=None, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Recipes'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        unique_together = ('recipe', 'author', 'category')

    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"