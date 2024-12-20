from django import forms
from recipes.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'author']
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание',
            'preparation_steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (минуты)',
            'image': 'Изображение',
            'author': 'Автор',
        }



class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']