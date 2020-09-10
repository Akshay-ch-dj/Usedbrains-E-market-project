# Generated by Django 3.1.1 on 2020-09-10 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_authentic', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]