# Generated by Django 3.2.8 on 2022-03-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_1', '0013_suggest_details_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggest_details',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
