# Generated by Django 2.2.1 on 2019-05-24 14:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5)])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=100)),
                ('elements', models.ManyToManyField(blank=True, to='jewellery.Elements')),
                ('theme', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jewellery.Theme')),
            ],
        ),
    ]
