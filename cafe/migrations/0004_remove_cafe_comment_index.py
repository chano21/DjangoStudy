# Generated by Django 3.1 on 2021-03-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_cafe_user_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='comment_index',
        ),
    ]
