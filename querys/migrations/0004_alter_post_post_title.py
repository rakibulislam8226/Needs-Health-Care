# Generated by Django 4.1.4 on 2022-12-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querys', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=255),
        ),
    ]