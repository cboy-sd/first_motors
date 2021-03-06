# Generated by Django 2.1.15 on 2022-04-27 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0008_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='uploads/products'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='uploads/team'),
        ),
    ]
