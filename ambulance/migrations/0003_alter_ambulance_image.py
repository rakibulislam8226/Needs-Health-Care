# Generated by Django 4.1.4 on 2023-02-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0002_alter_ambulance_driver_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ambulances'),
        ),
    ]
