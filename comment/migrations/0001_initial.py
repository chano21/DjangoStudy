# Generated by Django 3.1 on 2021-03-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('del_yn', models.CharField(blank=True, choices=[('Y', '예'), ('N', '아니오')], default='Y', max_length=24, null=True, verbose_name='삭제여부')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='업데이트일')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='생성일')),
                ('comment_index', models.AutoField(primary_key=True, serialize=False, verbose_name='Comment Index')),
                ('cafe_name', models.CharField(blank=True, max_length=24, null=True, verbose_name='댓글')),
            ],
            options={
                'verbose_name': '댓글',
                'db_table': 'study_comment',
                'managed': True,
            },
        ),
    ]
