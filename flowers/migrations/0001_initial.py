# Generated by Django 5.1.3 on 2024-12-12 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descriptions', models.TextField()),
                ('image', models.ImageField(upload_to='flowers/')),
                ('views', models.IntegerField(default=0)),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.types')),
            ],
        ),
    ]
