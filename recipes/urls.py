from django.urls import path, include
from recipes import views

app_name = 'rec'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('random-recipe/', views.random_recipe, name='random_recipe'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
]