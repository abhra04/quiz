# Generated by Django 3.2 on 2021-05-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20210506_2258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='score',
            new_name='scores',
        ),
    ]
