# Generated by Django 3.0.2 on 2020-01-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_artist_artist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_rating',
            field=models.IntegerField(default=0),
        ),
    ]
