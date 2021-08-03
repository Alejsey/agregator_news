# Generated by Django 3.2.5 on 2021-07-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('link', models.URLField()),
                ('date', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]