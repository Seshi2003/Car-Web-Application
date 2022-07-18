# Generated by Django 3.2.8 on 2022-03-03 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_1.car_info')),
            ],
        ),
    ]