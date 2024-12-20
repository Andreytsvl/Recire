from django.contrib import admin
from .models import Recipe, Category, RecipeCategory
from django.utils.translation import gettext_lazy as _

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'cooking_time', 'created_at')
    # list_filter = ('author', 'category')
    search_fields = ('title', 'author__username')

    # Для удобства добавим фильтрацию по категориям
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('author')


# admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(RecipeCategory)
