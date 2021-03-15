# Generated by Django 3.1 on 2021-03-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_comment_user_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='cafe_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_depth',
            field=models.IntegerField(blank=True, null=True, verbose_name='depth'),
        ),
    ]
