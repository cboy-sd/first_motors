# Generated by Django 2.1.15 on 2022-05-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0011_auto_20220427_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
