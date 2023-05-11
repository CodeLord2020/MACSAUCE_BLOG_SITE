# Generated by Django 4.1.7 on 2023-05-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_post_dislikes_post_hearts_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hearts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='heart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
