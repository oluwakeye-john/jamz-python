# Generated by Django 3.0.2 on 2020-01-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200103_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_cover',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(default='', max_length=255),
        ),
    ]
