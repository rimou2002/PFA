# Generated by Django 5.0.4 on 2024-05-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product_image2_product_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='salesnumber',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
