# Generated by Django 3.1 on 2021-07-16 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_detail_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='author_id',
        ),
    ]
