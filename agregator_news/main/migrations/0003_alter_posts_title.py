# Generated by Django 3.2.5 on 2021-07-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
