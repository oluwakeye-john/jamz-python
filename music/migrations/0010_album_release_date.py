# Generated by Django 3.0.2 on 2020-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_song_song_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]