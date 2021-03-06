# Generated by Django 3.2.5 on 2021-07-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210725_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.TextField(blank=True, default=str),
        ),
        migrations.AlterField(
            model_name='posts',
            name='link',
            field=models.URLField(blank=True, default=str),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True, default=str),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(blank=True, default=str, max_length=100),
        ),
    ]
