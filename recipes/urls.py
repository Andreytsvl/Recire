from django.urls import path, include
from recipes import views

app_name = 'recipes'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('random-recipe/', views.random_recipe, name='random_recipe'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('list-recipes/', views.list_recipes, name='list_recipes'),
    path('update-recipe/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
    path('delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('mono-recipe/<int:recipe_id>/', views.mono_recipe, name='mono_recipe'),
]