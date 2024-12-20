# Generated by Django 5.1.4 on 2024-12-20 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterUniqueTogether(
            name='recipecategory',
            unique_together={('recipe', 'author', 'category')},
        ),
    ]