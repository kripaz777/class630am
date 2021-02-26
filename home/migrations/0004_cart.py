# Generated by Django 3.1.6 on 2021-02-23 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=200)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.item')),
            ],
        ),
    ]