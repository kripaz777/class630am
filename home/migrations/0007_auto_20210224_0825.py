# Generated by Django 3.1.6 on 2021-02-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cart_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
