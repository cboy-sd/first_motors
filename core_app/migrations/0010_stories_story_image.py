# Generated by Django 2.1.15 on 2022-04-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0009_auto_20220427_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='story_image',
            field=models.ImageField(blank=True, upload_to='uploads/story/images'),
        ),
    ]