# Generated by Django 4.1.7 on 2023-04-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post_author_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Author',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
