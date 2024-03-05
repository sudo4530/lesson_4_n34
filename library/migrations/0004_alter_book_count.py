# Generated by Django 5.0.3 on 2024-03-05 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]