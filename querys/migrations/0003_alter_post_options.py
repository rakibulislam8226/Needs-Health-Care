# Generated by Django 4.1.4 on 2022-12-24 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('querys', '0002_remove_query_creator_delete_answer_delete_query'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
