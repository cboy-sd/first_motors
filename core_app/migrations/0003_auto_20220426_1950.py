# Generated by Django 2.1.15 on 2022-04-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_auto_20220426_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_story',
            name='image',
            field=models.ImageField(upload_to='static/company/images'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='static/services'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='static/team'),
        ),
    ]
