# Generated by Django 4.1.4 on 2023-02-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
