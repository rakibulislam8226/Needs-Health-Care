# Generated by Django 4.1.4 on 2023-01-26 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querys', '0004_alter_post_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerpost',
            old_name='post',
            new_name='post_from',
        ),
        migrations.RemoveField(
            model_name='post',
            name='answer',
        ),
        migrations.AddField(
            model_name='post',
            name='answer_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='querys.answerpost'),
            preserve_default=False,
        ),
    ]
