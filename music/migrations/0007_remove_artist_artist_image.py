# Generated by Django 3.0.2 on 2020-01-03 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200103_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_image',
        ),
    ]