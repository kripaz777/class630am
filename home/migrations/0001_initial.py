# Generated by Django 3.1.6 on 2021-02-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.TextField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('subject', models.TextField()),
                ('email', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('label', models.CharField(blank=True, choices=[('new', 'new'), ('hot', 'hot'), ('', 'default')], max_length=100)),
                ('slug', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=300)),
                ('stock', models.CharField(choices=[('in', 'IN Stock'), ('out', 'Out of stock')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.TextField()),
                ('text', models.TextField()),
                ('rank', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=200)),
            ],
        ),
    ]