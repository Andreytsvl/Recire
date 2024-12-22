from django import forms
from recipes.models import Recipe, Category

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
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Категории"
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'preparation_steps': forms.Textarea(attrs={'rows': 6}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }