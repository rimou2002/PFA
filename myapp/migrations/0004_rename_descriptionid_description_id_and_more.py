# Generated by Django 5.0.4 on 2024-05-01 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_password_admin_department_remove_admin_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='descriptionid',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categorie_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviews_id',
        ),
        migrations.AddField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.categorie'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.description'),
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.reviews'),
        ),
    ]
