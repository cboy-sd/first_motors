# Generated by Django 2.1.15 on 2022-04-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_auto_20220426_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_story',
            name='image',
            field=models.ImageField(upload_to='uploads/company'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='uploads/services'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='uploads/team'),
        ),
    ]
