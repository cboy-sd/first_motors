# Generated by Django 2.1.15 on 2022-04-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0010_stories_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services/'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='story_image',
            field=models.ImageField(blank=True, upload_to='story/images'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='team/'),
        ),
    ]
