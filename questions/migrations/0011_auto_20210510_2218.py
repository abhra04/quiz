# Generated by Django 3.2 on 2021-05-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20210510_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scores',
            name='difficulty',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
