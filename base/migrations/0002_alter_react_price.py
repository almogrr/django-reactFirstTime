# Generated by Django 5.0.2 on 2024-02-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]