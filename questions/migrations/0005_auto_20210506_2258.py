# Generated by Django 3.2 on 2021-05-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='response1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response10',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response7',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response8',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='response9',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
