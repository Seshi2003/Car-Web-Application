# Generated by Django 3.2.8 on 2022-05-26 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_1', '0017_alter_used_car_details_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_1.used_car_details')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
