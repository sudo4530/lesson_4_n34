# Generated by Django 5.0.3 on 2024-03-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
