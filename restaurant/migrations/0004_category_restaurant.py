# Generated by Django 4.0.3 on 2022-11-14 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
        ),
    ]
