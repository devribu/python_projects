# Generated by Django 3.2.13 on 2022-06-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='foto',
            field=models.ImageField(upload_to='pics2'),
        ),
    ]
